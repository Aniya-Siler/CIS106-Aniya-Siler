<?xml version="1.0"?>
<flowgorithm fileversion="3.0">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="cash america"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2022-09-09 07:40:38 PM"/>
        <attribute name="created" value="Y2FzaCBhbWVyaWNhO0FOSVlBU0NPTVBVVEVSOzIwMjItMDktMDk7MDc6MDk6MzUgUE07MzUzNw=="/>
        <attribute name="edited" value="Y2FzaCBhbWVyaWNhO0FOSVlBU0NPTVBVVEVSOzIwMjItMDktMDk7MDc6NDA6MzggUE07NTszNjQ3"/>
    </attributes>
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
</flowgorithm>
