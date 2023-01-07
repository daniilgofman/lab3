<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>BridgeBeam.py</Name>
        <Title>CreateBridgeBeam</Title>
        <Version>1.0</Version>
    </Script>

    <Page>
        <Name>Page3</Name>
        <Text>Polygon3D</Text>

        <Parameter>
            <Name>Color3</Name>
            <Text>Колір</Text>
            <Value>1</Value>
            <ValueType>Color</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator1</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>BeamLength</Name>
            <Text>Довжина балки </Text>
            <Value>12000.</Value>
            <MinValue>12000.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator2</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>TopShWidth</Name>
            <Text>Ширина верхньої частини балки </Text>
            <Value>600.</Value>
            <MinValue>600.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>BotShWidth</Name>
            <Text>Ширина нижньої частини балки </Text>
            <Value>480.</Value>
            <MinValue>480.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>RibThick</Name>
            <Text>Товщина ребра </Text>
            <Value>160.</Value>
            <MinValue>160.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator3</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>BeamHeight</Name>
            <Text>Висота балки </Text>
            <Value>1100.</Value>
            <MinValue>1100.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>BotShLowHeight</Name>
            <Text>Висота нижньої частини балки </Text>
            <Value>153.</Value>
            <MinValue>153.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>BotShUpHeight</Name>
            <Text>Висота середньої частини</Text>
            <Value>160.</Value>
            <MinValue>160.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>RibHeight</Name>
            <Text>Висота ребра </Text>
            <Value>467.</Value>
            <MinValue>467.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>TopShHeight</Name>
            <Text>Висота верхньої частини балки </Text>
            <Value>320.</Value>
            <MinValue>320.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator4</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>HoleDepth</Name>
            <Text>Глибина до строповочного отвору </Text>
            <Value>350.</Value>
            <MinValue>350.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>HoleHeight</Name>
            <Text>Висота до строповочного отвору </Text>
            <Value>540.</Value>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator5</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>CheckBoxV</Name>
            <Text>Додати переріз </Text>
            <Value>False</Value>
            <ValueType>CheckBox</ValueType>
        </Parameter>
        <Parameter>
            <Name>VaryingStart</Name>
            <Text>Початок зони зміни перерізу </Text>
            <Value>1500.</Value>
            <MinValue>100.</MinValue>
            <Visible>
if CheckBoxV:
    return True
return False
            </Visible>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>VaryingLength</Name>
            <Text>Довжина зони зміни перерізу </Text>
            <Value>1500.</Value>
            <MinValue>0</MinValue>
            <Visible>
if CheckBoxV:
    return True
return False
            </Visible>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>VaryingRibThick</Name>
            <Text>Товщина ребра центрального перерізу </Text>
            <Value>120.</Value>
            <MinValue>120.</MinValue>
            <Visible>
if CheckBoxV:
    return True
return False
            </Visible>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator6</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
                <Name>RotationAngleX</Name>
                <Text>Поворот відносно осі X </Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
            <Parameter>
                <Name>RotationAngleY</Name>
                <Text>Поворот відносно осі Y </Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
            <Parameter>
                <Name>RotationAngleZ</Name>
                <Text>Поворот відносно осі Z </Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
    </Page>    
</Element>
