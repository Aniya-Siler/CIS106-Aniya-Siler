    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Pay" type="Real" array="False" size=""/>
            <declare name="Hours" type="Real" array="False" size=""/>
            <declare name="Rate" type="Real" array="False" size=""/>
            <declare name="Annual" type="Real" array="False" size=""/>
            <declare name="Monthly" type="Real" array="False" size=""/>
            <output expression="(&quot;Enter hours:&quot;)" newline="True"/>
            <input variable="Hours"/>
            <output expression="(&quot;Enter Rate Per hour:&quot;)" newline="True"/>
            <input variable="Rate"/>
            <assign variable="Pay" expression="(Hours*Rate)"/>
            <output expression="&quot;Weekly Income&quot;" newline="False"/>
            <output expression="(Pay)" newline="True"/>
            <assign variable="Monthly" expression="(Pay*52/12)"/>
            <output expression="&quot;Monthly Income&quot;" newline="False"/>
            <output expression="(Monthly)" newline="True"/>
            <assign variable="Annual" expression="(Pay*52)"/>
            <output expression="&quot;Annual Income&quot;" newline="False"/>
            <output expression="(Annual)" newline="True"/>
        </body>
    </function>
