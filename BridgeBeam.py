


import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Utility as AllplanUtil
import GeometryValidate as GeometryValidate

from StdReinfShapeBuilder.RotationAngles import RotationAngles
from HandleDirection import HandleDirection
from HandleProperties import HandleProperties
from HandleService import HandleService

print('Load BridgeBeam.py')

def check_allplan_version(build_part, version):
    # Delete unused arguments
    del build_part
    del version


    return True

def create_element(build_part, doc):

    element = CreateBridgeBeam(doc)


    return element.create(build_part)

def move_handle(build_part, handle_property, input_pnt, doc):

    build_part.change_property(handle_property, input_pnt)

    if (handle_property.handle_id == "BeamHeight"):
        build_part.RibHeight.value = build_part.BeamHeight.value - build_part.TopShHeight.value - build_part.BotShLowHeight.value - build_part.BotShUpHeight.value
        if (build_part.HoleHeight.value > build_part.BeamHeight.value - build_part.TopShHeight.value - 45.5):
            build_part.HoleHeight.value = build_part.BeamHeight.value - build_part.TopShHeight.value - 45.5
    elif (handle_property.handle_id == "TopShWidth") or (handle_property.handle_id == "BotShWidth") or (handle_property.handle_id == "RibThick"):
        temp = min(build_part.TopShWidth.value, build_part.BotShWidth.value)
        if (build_part.RibThick.value >= temp - 100.):
            build_part.RibThick.value = temp - 100.
        if (build_part.RibThick.value <= build_part.VaryingRibThick.value):
            build_part.VaryingRibThick.value = build_part.RibThick.value - 20.
        elif (build_part.RibThick.value - 100. >= build_part.VaryingRibThick.value):
            build_part.VaryingRibThick.value = build_part.RibThick.value - 100.


    return create_element(build_part, doc)

def modify_element_property(build_part, name, value):

    if (name == "BeamHeight"):
        change = value - build_part.TopShHeight.value - build_part.RibHeight.value - build_part.BotShUpHeight.value - build_part.BotShLowHeight.value
        print(change)
        if (change < 0):
            change = abs(change)
            if (build_part.TopShHeight.value > 320.):
                if (build_part.TopShHeight.value - change < 320.):
                    change -= build_part.TopShHeight.value - 320.
                    build_part.TopShHeight.value = 320.
                else:
                    build_part.TopShHeight.value -= change
                    change = 0.
            if (change != 0) and (build_part.BotShUpHeight.value > 160.):
                if (build_part.BotShUpHeight.value - change < 160.):
                    change -= build_part.BotShUpHeight.value - 160.
                    build_part.BotShUpHeight.value = 160.
                else:
                    build_part.BotShUpHeight.value -= change
                    change = 0.
            if (change != 0) and (build_part.BotShLowHeight.value > 153.):
                if (build_part.BotShLowHeight.value - change < 153.):
                    change -= build_part.BotShLowHeight.value - 153.
                    build_part.BotShLowHeight.value = 153.
                else:
                    build_part.BotShLowHeight.value -= change
                    change = 0.
            if (change != 0) and (build_part.RibHeight.value > 467.):
                if (build_part.RibHeight.value - change < 467.):
                    change -= build_part.RibHeight.value - 467.
                    build_part.RibHeight.value = 467.
                else:
                    build_part.RibHeight.value -= change
                    change = 0.
        else:
            build_part.RibHeight.value += change
        if (value - build_part.TopShHeight.value - 45.5 < build_part.HoleHeight.value):
            build_part.HoleHeight.value = value - build_part.TopShHeight.value - 45.5
    elif (name == "TopShHeight"):
        build_part.BeamHeight.value = value + build_part.RibHeight.value + build_part.BotShUpHeight.value + build_part.BotShLowHeight.value
    elif (name == "RibHeight"):
        build_part.BeamHeight.value = value + build_part.TopShHeight.value + build_part.BotShUpHeight.value + build_part.BotShLowHeight.value
    elif (name == "BotShUpHeight"):
        build_part.BeamHeight.value = value + build_part.TopShHeight.value + build_part.RibHeight.value + build_part.BotShLowHeight.value
        temp = value + build_part.BotShLowHeight.value + 45.5
        if (temp > build_part.HoleHeight.value):
            build_part.HoleHeight.value = temp
    elif (name == "BotShLowHeight"):
        build_part.BeamHeight.value = value + build_part.TopShHeight.value + build_part.RibHeight.value + build_part.BotShUpHeight.value
        temp = build_part.BotShUpHeight.value + value + 45.5
        if (temp > build_part.HoleHeight.value):
            build_part.HoleHeight.value = temp
    elif (name == "HoleHeight"):
        temp = build_part.BeamHeight.value - build_part.TopShHeight.value - 45.5
        temp1 = build_part.BotShLowHeight.value + build_part.BotShUpHeight.value + 45.5
        if (value > temp):
            build_part.HoleHeight.value = temp
        elif (value < temp1):
            build_part.HoleHeight.value = temp1
    elif (name == "HoleDepth") and (value >= build_part.BeamLength.value / 2.):
        build_part.HoleDepth.value = build_part.BeamLength.value / 2. - 45.5
    elif (name == "TopShWidth") or (name == "BotShWidth") or (name == "RibThick"):
        temp = min(build_part.TopShWidth.value, build_part.BotShWidth.value)
        if (build_part.RibThick.value >= temp - 100.):
            build_part.RibThick.value = temp - 100.
        if (value <= build_part.VaryingRibThick.value):
            build_part.VaryingRibThick.value = build_part.RibThick.value - 20.
        elif (value - 100. >= build_part.VaryingRibThick.value):
            build_part.VaryingRibThick.value = build_part.RibThick.value - 100.
    elif (name == "VaryingStart"):
        temp = build_part.BeamLength.value / 2.
        if (value >= temp):
            build_part.VaryingStart.value = temp - 200.
        temp -= build_part.VaryingStart.value
        if (build_part.VaryingLength.value >= temp):
            build_part.VaryingLength.value = temp - 100.
    elif (name == "VaryingLength"):
        temp = build_part.BeamLength.value / 2. - build_part.VaryingStart.value
        if (value >= temp):
            build_part.VaryingLength.value = temp - 100.
    elif (name == "VaryingRibThick"):
        if (value >= build_part.RibThick.value):
            build_part.VaryingRibThick.value = build_part.RibThick.value - 20.
        elif (value <= build_part.RibThick.value - 100.):
            build_part.VaryingRibThick.value = build_part.RibThick.value - 100.

    return True

class CreateBridgeBeam():
    def __init__(self, doc):

        self.model_parts_list = []
        self.handle_list = []
        self.document = doc
        
    def create(self, build_part):
                
        self._top_sh_width = build_part.TopShWidth.value
        self._top_sh_height = build_part.TopShHeight.value

        self._bot_sh_width = build_part.BotShWidth.value
        self._bot_sh_up_height = build_part.BotShUpHeight.value
        self._bot_sh_low_height = build_part.BotShLowHeight.value
        self._bot_sh_height = self._bot_sh_up_height + self._bot_sh_low_height
        
        self._rib_thickness = build_part.RibThick.value
        self._rib_height = build_part.RibHeight.value

        self._varying_start = build_part.VaryingStart.value
        self._varying_length = build_part.VaryingLength.value
        self._varying_end = self._varying_start + self._varying_length
        self._varying_rib_thickness = build_part.VaryingRibThick.value

        self._beam_length = build_part.BeamLength.value
        self._beam_width = max(self._top_sh_width, self._bot_sh_width)
        self._beam_height = build_part.BeamHeight.value

        self._hole_depth = build_part.HoleDepth.value
        self._hole_height = build_part.HoleHeight.value

        self._angleX = build_part.RotationAngleX.value
        self._angleY = build_part.RotationAngleY.value
        self._angleZ = build_part.RotationAngleZ.value

        self.create_beam(build_part)
        self.create_handles(build_part)
        
        AllplanBaseElements.ElementTransform(AllplanGeo.Vector3D(), self._angleX, self._angleY, self._angleZ, self.model_parts_list)

        rot_angles = RotationAngles(self._angleX, self._angleY, self._angleZ)
        HandleService.transform_handles(self.handle_list, rot_angles.get_rotation_matrix())
        
        return (self.model_parts_list, self.handle_list)

    def create_beam(self, build_part):
        com_prop = AllplanBaseElements.CommonProperties()
        com_prop.GetGlobalProperties()
        com_prop.Pen = 1
        com_prop.Color = build_part.Color3.value
        com_prop.Stroke = 1

        breps = AllplanGeo.BRep3DList()

        bottom_shelf = AllplanGeo.BRep3D.CreateCuboid(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D((self._beam_width - self._bot_sh_width) / 2., 0., 0.), AllplanGeo.Vector3D(1, 0, 0), AllplanGeo.Vector3D(0, 0, 1)), self._bot_sh_width / 2., self._beam_length / 2., self._bot_sh_height)

        edges = AllplanUtil.VecSizeTList()
        edges.append(10)
        err, bottom_shelf = AllplanGeo.ChamferCalculus.Calculate(bottom_shelf, edges, 20., False)
        if not GeometryValidate.polyhedron(err):
            return        
        breps.append(bottom_shelf)
        

        top_shelf = AllplanGeo.BRep3D.CreateCuboid(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D((self._beam_width - self._top_sh_width) / 2., 0., self._beam_height - self._top_sh_height), AllplanGeo.Vector3D(1, 0, 0), AllplanGeo.Vector3D(0, 0, 1)), self._top_sh_width / 2., self._beam_length / 2., self._top_sh_height)

        top_shelf_notch = AllplanGeo.BRep3D.CreateCuboid(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D((self._beam_width - self._top_sh_width) / 2., 0., self._beam_height - 45.), AllplanGeo.Vector3D(1, 0, 0), AllplanGeo.Vector3D(0, 0, 1)), 60., self._beam_length  / 2., 45.)
        err, top_shelf = AllplanGeo.MakeSubtraction(top_shelf, top_shelf_notch)
        if not GeometryValidate.polyhedron(err):
            return
        breps.append(top_shelf)
        

        rib = AllplanGeo.BRep3D.CreateCuboid(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(0., 0., self._bot_sh_height), AllplanGeo.Vector3D(1, 0, 0), AllplanGeo.Vector3D(0, 0, 1)), self._beam_width / 2., self._beam_length / 2., self._rib_height)
        breps.append(rib)
        
        err, beam = AllplanGeo.MakeUnion(breps)
        if not GeometryValidate.polyhedron(err):
            return


        breps = AllplanGeo.BRep3DList()                
        notch_pol = AllplanGeo.Polyline3D()
        start_point = AllplanGeo.Point3D((self._beam_width - self._rib_thickness) / 2., 0., self._beam_height - self._top_sh_height)
        notch_pol += start_point
        notch_pol += AllplanGeo.Point3D((self._beam_width - self._rib_thickness) / 2., 0., self._bot_sh_height)
        notch_pol += AllplanGeo.Point3D((self._beam_width - self._bot_sh_width) / 2., 0., self._bot_sh_low_height)
        notch_pol += AllplanGeo.Point3D(-10., 0., self._bot_sh_low_height)     
        notch_pol += AllplanGeo.Point3D(-10., 0., self._beam_height - 100.)
        notch_pol += AllplanGeo.Point3D((self._beam_width - self._top_sh_width) / 2., 0., self._beam_height - 100.)
        notch_pol += start_point
        if not GeometryValidate.is_valid(notch_pol):
            return

        path = AllplanGeo.Polyline3D()
        path += AllplanGeo.Point3D(0, 0, 0)
        path += AllplanGeo.Point3D(0, self._varying_start, 0) if build_part.CheckBoxV.value else AllplanGeo.Point3D(0, self._beam_length / 2., 0)
        
        err, notch = AllplanGeo.CreateSweptBRep3D(notch_pol, path, False, None)
        if not GeometryValidate.polyhedron(err):
            return
        edges = AllplanUtil.VecSizeTList()
        edges.append(3)
        edges.append(1)
        err, notch = AllplanGeo.FilletCalculus3D.Calculate(notch, edges, 100., False)
        if not GeometryValidate.polyhedron(err):
            return
        breps.append(notch)


        if build_part.CheckBoxV.value:
            profiles = []
            profiles.append(AllplanGeo.Move(notch_pol, AllplanGeo.Vector3D(0, self._varying_start, 0)))
                    
            lines = []
            lines.append(AllplanGeo.Line3D(notch_pol.GetPoint(0), notch_pol.GetPoint(5)))
            lines.append(AllplanGeo.Line3D(notch_pol.GetPoint(1), notch_pol.GetPoint(2)))
            lines.append(AllplanGeo.Move(AllplanGeo.Line3D(notch_pol.GetPoint(0), notch_pol.GetPoint(1)), AllplanGeo.Vector3D((self._rib_thickness - self._varying_rib_thickness) / 2., 0, 0)))
            intersections = [None,None]
            b, intersections[0] = AllplanGeo.IntersectionCalculusEx(lines[0], lines[2])
            b, intersections[1] = AllplanGeo.IntersectionCalculusEx(lines[1], lines[2])
                        
            notch_pol = AllplanGeo.Polyline3D()
            start_point = AllplanGeo.Point3D((self._beam_width - self._varying_rib_thickness) / 2., self._varying_end, intersections[0].Z)
            notch_pol += start_point
            notch_pol += AllplanGeo.Point3D((self._beam_width - self._varying_rib_thickness) / 2., self._varying_end, intersections[1].Z)
            notch_pol += AllplanGeo.Point3D((self._beam_width - self._bot_sh_width) / 2., self._varying_end, self._bot_sh_low_height)
            notch_pol += AllplanGeo.Point3D(-10., self._varying_end, self._bot_sh_low_height)     
            notch_pol += AllplanGeo.Point3D(-10., self._varying_end, self._beam_height - 100.)
            notch_pol += AllplanGeo.Point3D((self._beam_width - self._top_sh_width) / 2., self._varying_end, self._beam_height - 100.)
            notch_pol += start_point
            if not GeometryValidate.is_valid(notch_pol):
                return
            
            path = AllplanGeo.Polyline3D()
            path += AllplanGeo.Point3D(0, self._varying_end, 0)
            path += AllplanGeo.Point3D(0, self._beam_length / 2., 0)

            err, notch = AllplanGeo.CreateSweptBRep3D(notch_pol, path, False, None)
            if not GeometryValidate.polyhedron(err):
                return
            err, notch = AllplanGeo.FilletCalculus3D.Calculate(notch, edges, 100., False)
            if not GeometryValidate.polyhedron(err):
                return
            breps.append(notch)

            profiles.append(notch_pol)
            path = AllplanGeo.Line3D(profiles[0].GetStartPoint(), profiles[1].GetStartPoint())

            err, notch = AllplanGeo.CreateRailSweptBRep3D(profiles, [path], True, False, False)

            edges = AllplanUtil.VecSizeTList()
            edges.append(11)
            edges.append(9)
            err, notch = AllplanGeo.FilletCalculus3D.Calculate(notch, edges, 100., False)
            if not GeometryValidate.polyhedron(err):
                return
            breps.append(notch)


        sling_hole = AllplanGeo.BRep3D.CreateCylinder(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(0, build_part.HoleDepth.value, build_part.HoleHeight.value), AllplanGeo.Vector3D(0, 0, 1), AllplanGeo.Vector3D(1, 0, 0)), 45.5, self._beam_width)
        breps.append(sling_hole)
        
        err, beam = AllplanGeo.MakeSubtraction(beam, breps)
        if not GeometryValidate.polyhedron(err):
            return


        plane = AllplanGeo.Plane3D(AllplanGeo.Point3D(self._beam_width / 2., 0, 0), AllplanGeo.Vector3D(1, 0, 0))
        err, beam = AllplanGeo.MakeUnion(beam, AllplanGeo.Mirror(beam, plane))
        if not GeometryValidate.polyhedron(err):
            return
        plane.Set(AllplanGeo.Point3D(0, self._beam_length / 2., 0), AllplanGeo.Vector3D(0, 1, 0))
        err, beam = AllplanGeo.MakeUnion(beam, AllplanGeo.Mirror(beam, plane))
        if not GeometryValidate.polyhedron(err):
            return
        self.model_parts_list.append(AllplanBasisElements.ModelElement3D(com_prop, beam))

    def create_handles(self, build_part):

        handle1 = HandleProperties("BeamLength",
                                   AllplanGeo.Point3D(0., self._beam_length, 0.),
                                   AllplanGeo.Point3D(0, 0, 0),
                                   [("BeamLength", HandleDirection.point_dir)],
                                   HandleDirection.point_dir, True)
        self.handle_list.append(handle1)

        handle2 = HandleProperties("BeamHeight",
                                   AllplanGeo.Point3D(0., 0., self._beam_height),
                                   AllplanGeo.Point3D(0, 0, 0),
                                   [("BeamHeight", HandleDirection.point_dir)],
                                   HandleDirection.point_dir, True)
        self.handle_list.append(handle2)
        
        handle3 = HandleProperties("TopShWidth",
                                   AllplanGeo.Point3D((self._beam_width - self._top_sh_width) / 2. + self._top_sh_width, 0., self._beam_height - 45.),
                                   AllplanGeo.Point3D((self._beam_width - self._top_sh_width) / 2., 0, self._beam_height - 45.),
                                   [("TopShWidth", HandleDirection.point_dir)],
                                   HandleDirection.point_dir, True)
        self.handle_list.append(handle3)

        handle4 = HandleProperties("BotShWidth",
                                   AllplanGeo.Point3D((self._beam_width - self._bot_sh_width) / 2. + self._bot_sh_width, 0., self._bot_sh_low_height),
                                   AllplanGeo.Point3D((self._beam_width - self._bot_sh_width) / 2., 0, self._bot_sh_low_height),
                                   [("BotShWidth", HandleDirection.point_dir)],
                                   HandleDirection.point_dir, True)
        self.handle_list.append(handle4)
        
        handle5 = HandleProperties("RibThick",
                                   AllplanGeo.Point3D((self._beam_width - self._rib_thickness) / 2. + self._rib_thickness, 0., self._beam_height / 2.),
                                   AllplanGeo.Point3D((self._beam_width - self._rib_thickness) / 2., 0, self._beam_height / 2.),
                                   [("RibThick", HandleDirection.point_dir)],
                                   HandleDirection.point_dir, True)
        self.handle_list.append(handle5)

        