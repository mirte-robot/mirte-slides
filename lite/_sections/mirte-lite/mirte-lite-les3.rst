**MIRTE** lite 
==========================

Les 3: Wielen en elektronica

.. revealjs-section::
   :data-background-image: _static/media/mirte-lite/mirte-lite-les1/mirte-ingekleurd-op-lijn.png


**Doel**
--------------------

.. container:: smaller70

   In deze les leer je alles over wielen. Ook leer je wat een stroomkring is en hoe je de elektronica van de robot moet aansluiten, zodat de robot zelfstandig kan rijden.


**Functie van een wiel**
--------------------

.. container:: smaller70

    De functie van een wiel is om transport makkelijker te maken. Zo kunnen grote objecten gemakkelijk worden vervoerd en kunnen mensen sneller van A naar B. 

.. raw:: html
   
   <div class="popup">
   <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/trafic-pexels-vladfonsark.jpg" style="width:auto; height:300px;">
   <span class="popuptext smaller40">Foto door Vlad Fonsark via <a href="https://www.pexels.com/photo/tram-and-cars-in-traffic-jam-at-rush-hour-4993448/">Pexels</a></span>
   </div>


**Soorten wielen**
--------------------

.. container:: smaller70

    Wat zouden de voordelen van deze wielen kunnen zijn?

.. raw:: html

    <!DOCTYPE html>
    <html>
    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
    <div class="popup_copyright">
        <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/autowiel-unsplash-alexandrbendus.jpg" style="width:250px; height:auto;">
        <span class="popuptext smaller40">Autowielen hebben over het algemeen veel grip met de weg, waardoor een auto niet makkelijk kan uitglijden.<br><i>Foto door Александр Бендус via <a href="https://unsplash.com/photos/a-couple-of-cars-parked-next-to-each-other-1EfzQlH8yMo/">Unsplash</a></i></span>
        </div>
    <div style="clear: both;"></div>
    
    <div class="smaller50">autowiel</div>

    </div>

    <div class="column">
    <div class="popup_copyright">
        <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/zwenkwiel-unsplash-americangreentravel.jpg" style="width:250px; height:auto;">
        <span class="popuptext smaller40">Zwenkwielen kunnen van richting veranderen, waardoor je er goed mee kunt sturen.<br><i>Foto door American Green Travel via <a href="https://unsplash.com/photos/a-piece-of-luggage-sitting-on-top-of-a-wooden-floor-VqLqFGdy4mg/">Unsplash</a></i></span>
        </div>
    <div style="clear: both;"></div>

    <div class="smaller50">zwenkwiel</div>

    </div>

    <div class="column">
    <div class="popup_copyright">
        <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/rupsband-unsplash-izzuddinazzam.jpg" style="width:250px; height:auto;">
        <span class="popuptext smaller40">Rupsbanden kunnen op allerlei soorten tereinen rijden, zonder dat de banden wegzakken in de grond.<br><i>Foto door Izzuddin Azzam via <a href="https://unsplash.com/photos/a-row-of-yellow-and-blue-construction-machines-HKBtu2w52DA/">Unsplash</a></i></span>
        </div>
    <div style="clear: both;"></div>

    <div class="smaller50">rupsband</div>

    </div>

    </body>

    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
    <div class="popup_copyright">
        <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/mirte-master.jpg" style="width:250px; height:auto;">
        <span class="popuptext smaller40">Mecanum wielen kunnen zowel naar voren en achteren, als naar links en rechts bewegen. Zo kan een robot ook zijdelings bewegen.</span>
        </div>
    <div style="clear: both;"></div>

    <div class="smaller50">mecanum wiel</div>

    </div>

   <div class="column">
    <div class="popup_copyright">
        <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/fietswiel-pexels-bluebird.jpg" style="width:250px; height:auto;">
        <span class="popuptext smaller40">Fietswielen zijn licht van gewicht en kunnen makkelijk gerepareerd worden. <br><i>Foto door Blue Bird via <a href="https://www.pexels.com/photo/crop-woman-with-bicycle-walking-on-urban-pavement-7242946/">Pexels</a></i></span>
        </div>
    <div style="clear: both;"></div>

    <div class="smaller50">fietswiel</div>

    </div>

    <div class="column">
    <div class="popup_copyright">
        <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/kogelwiel_foto.jpg" style="width:250px; height:auto;">
        <span class="popuptext smaller40">Een kogelwiel biedt extra ondersteuning en kan alle kanten op rollen.</span>
        </div>
    <div style="clear: both;"></div>

    <div class="smaller50">kogelwiel</div>

    </div>

    </body>
    </html>


**Welke wielen heeft MIRTE?**
--------------------

.. container:: smaller70

    Kijk goed naar jouw MIRTE robot. Op welke soort wielen lijken de wielen van jouw robot het meest? Er zijn twee antwoorden goed.

.. raw:: html

   <div class="grid-container3">
        <button class="button3"><img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/autowiel-unsplash-alexandrbendus.jpg"; style="width:auto; height:150px">
        <div>autowiel</div></button>
        <button class="button4"><img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/zwenkwiel-unsplash-americangreentravel.jpg"; style="width:auto; height:150px">
        <div>zwenkwiel</div></button>
        <button class="button4"><img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/rupsband-unsplash-izzuddinazzam.jpg"; style="width:auto; height:150px">
        <div>rupsband</div></button>
        <button class="button4"><img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/mirte-master.jpg"; style="width:auto; height:150px">
        <div>mecanum wiel</div></button>
        <button class="button4"><img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/fietswiel-pexels-bluebird.jpg"; style="width:auto; height:150px">
        <div>fietswiel</div></button>
        <button class="button3"><img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/kogelwiel_foto.jpg"; style="width:auto; height:150px">
        <div>kogelwiel</div></button>
   </div>


**Aantal wielen**
--------------------

.. container:: smaller70

    Een auto heeft normaal gesproken 4 wielen. Een vrachtwagen kan er zelfs wel 10 hebben. MIRTE heeft net zoals zonneauto Nuna maar 3 wielen. Wat zouden voor Nuna de voordelen kunnen zijn? Er zijn 2 antwoorden goed.


.. raw:: html

    <div class="popup">
     <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/nuna11s-ssc2022-jorritlousberg.jpg" style="width:auto; height:180px;">
     <span class="popuptext smaller40">Bij Nuna draait alles om duurzaamheid en efficiëntie. De beste zonnepanelen zorgen ervoor dat er meer energie opgewekt kan worden. Als de auto minder weegt, is er minder kracht en energie nodig om de auto vooruit te laten bewegen. Zo min mogelijk wrijving met de grond zorgt ervoor dat Nuna minder energie verbruikt tijdens het rijden. <br><i>© 2022 Brunel Solar Team. Foto door Jorrit Lousberg. <a href="https://www.tudelft.nl/2019/tu-delft/zwerm-kleine-drones-verkent-onbekende-omgeving#:~:text=Inspiratie%20uit%20de%20natuur,vallen%20van%20grote%2C%20individuele%20robots."></i></a></span>
    </div>

.. raw:: html

      <div class="grid-container">
        <button class="button2">A. 3 wielen zijn veiliger dan 4 wielen</button>
        <button class="button1">B. er is minder weerstand met de grond</button>
        <button class="button1">C. het bespaart gewicht</button>
        <button class="button2">D. er zijn minder banden nodig, waardoor het goedkoper is</button>
      </div>


**Aantal wielen**
--------------------

.. container:: smaller70

    Wat zou een nadeel kunnen zijn voor Nuna voor het hebben van maar 3 wielen? En hoe kun je dit oplossen? Het antwoord is te vinden op de volgende slide.


**Stabiliteit**
--------------------

.. container:: smaller70

    Om ervoor te zorgen dat een auto met 3 wielen toch stabiel is, moet het grootste gewicht binnen de steunpunten met de grond ligt. MIRTE steunt op de grond met behulp van de wielen. Voor MIRTE is het daarom belangrijk dat de batterij en breadboard binnen het gele vlak liggen, omdat dit de zwaarste onderdelen zijn. Leg de batterij maar eens voorop tussen de twee sensoren in. Wat gebeurt er nu?

.. image:: _static/media/mirte-lite/mirte-lite-les3/gewichtverdeling-mirte.png
   :width: 250px


**Wat is een stroomkring?**
--------------------

.. container:: smaller70

   In deze video van Schooltv.nl wordt uitgelegd wat een stroomkring is.

.. raw:: html

  <iframe src="https://player.ntr.nl/index.php?id=WO_NTR_12999150" width="600" height="338" frameborder="0" allow="encrypted-media; geolocation" allowfullscreen=""></iframe>


**Stroomkring test**
--------------------

.. container:: smaller70

   Op de volgende slides staat steeds een ander stroomkring afgebeeld, die jij mag namaken met de rechter motor en wiel van de robot en een batterij. Geef vervolgens aan welke stellingen waar zijn voor de stroomkring die jij hebt gemaakt. Tip: zet jouw robot op een verhoging, zodat de robot niet weg kan rijden.


**Stroomkring test**
--------------------

.. container:: smaller70

   Houd de rode kabel van de motor tegen de pluspool van de batterij en de zwarte kabel tegen de minpool van de batterij. Welke 2 stellingen zijn waar?

.. raw:: html

   <!DOCTYPE html>
    <html>
    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/stroomkring-a.png" style="width:auto; height:300px;">

    </div>

    <div class="column">
    <div class="grid-container">
      <button class="button1">A. het wiel draait rechtsom</button>
      <button class="button2">B. het wiel draait linksom</button>
      <button class="button1">C. de stroomkring is gesloten</button>
      <button class="button2">D. de stroomkring is onderbroken</button>
    </div>

    </div>

    </body>
 

**Stroomkring test**
--------------------

.. container:: smaller70

   Houd de zwarte kabel van de motor tegen de pluspool van de batterij en de rode kabel tegen de minpool van de batterij. Welke 2 stellingen zijn waar?

.. raw:: html

    <!DOCTYPE html>
    <html>
    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/stroomkring-b.png" style="width:auto; height:300px;">

    </div>

    <div class="column">
    <div class="grid-container">
      <button class="button2">A. het wiel draait rechtsom</button>
      <button class="button1">B. het wiel draait linksom</button>
      <button class="button1">C. de stroomkring is gesloten</button>
      <button class="button2">D. de stroomkring is onderbroken</button>
    </div>

    </div>

    </body>

**Stroomkring test**
--------------------

.. container:: smaller70

   Houd de zwarte kabel van de motor tegen de minpool van de batterij en zorg ervoor dat de rode kabel de batterij niet aanraakt. Welke 2 stellingen zijn waar?

.. raw:: html

       <!DOCTYPE html>
    <html>
    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/stroomkring-c.png" style="width:auto; height:300px;">

    </div>

    <div class="column">
    <div class="grid-container">
      <button class="button2">A. het wiel draait</button>
      <button class="button1">B. het wiel draait niet</button>
      <button class="button2">C. de stroomkring is gesloten</button>
      <button class="button1">D. de stroomkring is onderbroken</button>
    </div>

    </div>

    </body>


**Elektronica aansluiten**
--------------------

.. container:: smaller70

   Nu gaan we de elektronica van de MIRTE robot aansluiten. Hiervoor heb je de volgende onderdelen nodig:

   .. raw:: html

    <!DOCTYPE html>
    <html>
    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/male_male.png" style="width:auto; height:200px;">
    <div style="clear: both;"></div>
    
    <div class="smaller40">4x kabel</div>

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/male_female.png" style="width:auto; height:200px;">
    <div style="clear: both;"></div>

    <div class="smaller40">6x kabel</div>

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les2/schroevendraaier.png" style="width:auto; height:200px;">
    <div style="clear: both;"></div>

    <div class="smaller40">schroevendraaier</div>

    </div>

    </body>


**Motoren aansluiten**
--------------------

.. container:: smaller70

   Begin met het vastmaken van de kabels van de motoren aan de motor driver. Zorg ervoor dat de kabels in de goede volgorde vastgemaakt worden. Gebruik een schroevendraaier om de kabels vast te zetten in de motor driver.

   .. raw:: html

    <!DOCTYPE html>
    <html>
    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/motor_driver_explanation.png" style="width:auto; height:250px;">

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/elektronica-schema-motoren.png" style="width:auto; height:200px;">

    </div>

    </body>


**Motor driver aansluiten**
--------------------

.. container:: smaller70

   Verbind de motor driver met het breadboard. Gebruik hiervoor de kabels met aan beide kanten een metalen uiteinde.

   .. raw:: html

    <!DOCTYPE html>
    <html>
    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
     <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/male_male.png" style="width:auto; height:200px;">
    <div style="clear: both;"></div>
    
    <div class="smaller40">4x</div>

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/elektronica-schema-motordriver.png" style="width:auto; height:200;">

    </div>

    </body>


**Sensoren aansluiten**
--------------------

.. container:: smaller70

   Verbind de obstakel sensoren met het breadboard. Gebruik hiervoor de kabels met maar 1 metalen uiteinde. 

   .. raw:: html

    <!DOCTYPE html>
    <html>
    <head>
    <style>

    .column {
    flex: 1;
    padding: 10px;
    }

    .row {
    display: flex;
    justify-content: center;
    }
    </style>
    </head>
    <body>

    <div class="row">
    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/male_female.png" style="width:auto; height:200px;">
    <div style="clear: both;"></div>

    <div class="smaller40">6x</div>

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les3/elektronica-schema-sensoren.png" style="width:600px; height:auto;">

    </div>

    </body>


**Krachtbron aansluiten**
--------------------

.. container:: smaller70

   Om het stroomschema compleet te maken, moet alleen de krachtbron nog aangesloten worden. Let op! Zorg ervoor dat de rode kabel op de plus kant van het breadboard wordt aangesloten en de zwarte kabel op de min kant. Zorg er ook voor dat de batterijhouder uitgeschakeld (OFF) is.

.. image:: _static/media/mirte-lite/mirte-lite-les3/elektronica-schema-compleet.png
   :width: 500px


**Robot testen**
--------------------

.. container:: smaller70

   Als je alles hebt aangesloten, kun je nu de robot testen. Til de robot op en schuif het knopje op de batterijhouder van OFF naar ON om de stroomkring te sluiten. Als het goed is draaien nu beide wielen naar voren. Houd nu je hand voor de rechter obstakelsensor. Het linker wiel stopt nu met draaien. Houd vervolgens je hand voor de linker obstakelsensor. Nu stopt het rechter wiel met draaien.

.. raw:: html

   <div class="popup">
   <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les1/informatie-vraagteken.png" style="width:auto; height:50px;">
   <span class="popuptext smaller40">Draaien de wielen naar achter? Draai dan de rode en zwarte kabel van de motor bij de motordriver om. <br>Draaien de wielen helemaal niet? Controleer of alle kabels goed aangesloten zijn en of de batterijen vol zijn.</span>
   </div>

**Volgende stap**
--------------------

.. revealjs-section::
   :data-background-image: _static/media/mirte-lite/mirte-lite-les1/mirte-end-of-line.png

.. container:: smaller70
  
   Uitstekend! Je hebt de derde les afgerond. Nu kun je door naar les 4.

.. raw:: html

    <button class="buttonback" onclick="Reveal.slide(3,0)">Terug naar het begin</button>
    <button class="buttonback" onclick="Reveal.slide(4,0)">Door naar les 4</button>