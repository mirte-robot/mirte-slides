**MIRTE** lite 
==========================

Les 4: Elektronica aansluiten

.. revealjs-section::
   :data-background-image: _static/media/mirte-lite/mirte-lite-les1/mirte-ingekleurd-op-lijn.png


**Doel**
--------------------

.. container:: smaller70

   In deze les leer je wat een stroomkring is en hoe je de elektronica van de robot moet aansluiten, zodat de robot zelfstandig kan rijden.


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
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/stroomkring-a.png" style="width:auto; height:300px;">

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
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/stroomkring-b.png" style="width:auto; height:300px;">

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
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/stroomkring-c.png" style="width:auto; height:300px;">

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
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/male_male.png" style="width:auto; height:200px;">
    <div style="clear: both;"></div>
    
    <div class="smaller40">4x kabel</div>

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/male_female.png" style="width:auto; height:200px;">
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
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/motor_driver_explanation.png" style="width:auto; height:250px;">

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/elektronica-schema-motoren.png" style="width:auto; height:200px;">

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
     <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/male_male.png" style="width:auto; height:200px;">
    <div style="clear: both;"></div>
    
    <div class="smaller40">4x</div>

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/elektronica-schema-motor-driver.png" style="width:auto; height:200;">

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
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/male_female.png" style="width:auto; height:200px;">
    <div style="clear: both;"></div>

    <div class="smaller40">6x</div>

    </div>

    <div class="column">
    <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les4/elektronica-schema-sensoren.png" style="width:600px; height:auto;">

    </div>

    </body>


**Krachtbron aansluiten**
--------------------

.. container:: smaller70

   Om het stroomschema compleet te maken, moet alleen de krachtbron nog aangesloten worden. Let op! Zorg ervoor dat de rode kabel op de plus kant van het breadboard wordt aangesloten en de zwarte kabel op de min kant. Zorg er ook voor dat de batterijhouder uitgeschakeld (OFF) is.

.. image:: _static/media/mirte-lite/mirte-lite-les4/elektronica_schema_compleet.png
   :width: 500px


**Robot testen**
--------------------

.. container:: smaller70

   Als je alles hebt aangesloten, kun je nu de robot testen. Til de robot op en schuif het knopje op de batterijhouder van OFF naar ON om de stroomkring te sluiten. Houd nu je hand voor de rechter obstakel sensor. Als het goed is, draait het rechter wiel nu naar voren. Houd vervolgens je hand voor de linker obstakel sensor. Nu hoort het rechter wiel te stoppen met draaien en zou het linker wiel naar voren moeten gaan draaien. 

.. raw:: html

   <div class="popup">
   <img loading="lazy" src="_static/media/mirte-lite/mirte-lite-les1/informatie-vraagteken.png" style="width:auto; height:50px;">
   <span class="popuptext smaller40">Draaien de wielen de verkeerde kant op? Controleer of je de motoren in de goede volgorde hebt aangesloten. <br>Draaien de wielen helemaal niet? Controleer of alle kabels goed aangesloten zijn en of de batterijen vol zijn.</span>
   </div>

**Volgende stap**
--------------------

.. revealjs-section::
   :data-background-image: _static/media/mirte-lite/mirte-lite-les1/mirte-end-of-line.png

.. container:: smaller70
  
   Uitstekend! Je hebt de vierde les afgerond. Nu kun je door naar les 5.

.. raw:: html

    <button class="buttonback" onclick="Reveal.slide(4,0)">Terug naar het begin</button>
    <button class="buttonback" onclick="Reveal.slide(5,0)">Door naar les 5</button>