Robotics Engineering
==========================



 .. raw:: html


    <button onclick="myFunction()">Try it</button>
    <div id='drawing'></div>
    <script>
    function myFunction() {
      //path.animate({duration: 1000}).attr({ d: 'M 25,0 h25 v25 h-25 v-25' })
      //path.animate({duration: 1000}).attr({ d: 'M 25,0 a10,10 0 0,0 -25,25 h10 a20,20 0 0,1 15,-15 v-10' })
      inner.animate({duration: 1000}).attr({'stroke-width': 16}).move(60,60);
      rect.animate({duration: 1000}).move(52,52);
    }

    var draw = SVG().addTo('#drawing').size('100%', '100%').viewbox(0,0,1000,1000);
    var inner = draw.circle(100).attr({ "fill": "none", "stroke": " #FBB927", "stroke-width":"100"}).move(8,8);
    var rect = draw.rect(58, 58);
    inner.clipWith(rect);

    //var path = draw.path('M 25,0 h25 v25 h-25 v-25')
    //var path = draw.path('M 25,0 a25,25 0 0,0 -25,25 h10 a15,15 0 0,1 15,-15 v-10')
    //path.attr({ fill: '#f03' })
    
    
    </script>
    
    



**MIRTE** family
==========================

Scroll down! 


**MIRTE** light
--------------------

.. container:: flex-container

   .. container:: half

      **MIRTE** light

   .. container:: half

      .. figure:: _static/mirte-light.png
         :width: 600

**MIRTE** basic
--------------------

.. container:: flex-container

   .. container:: half

      **MIRTE** light

   .. container:: half

      .. figure:: _static/mirte-light.png
         :width: 600


**MIRTE** pioneer
--------------------


**MIRTE** IDE
-------------


**MIRTE** Hardware
------------------

