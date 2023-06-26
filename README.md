# Radiant Escape Stundenprotokoll

<h2>Woche 1 (13.02. - 19.02.)</h2>

  
  Wir konkretisierten unsere Projektidee. Wir haben uns entschieden, ein Jump'n'Run Spiel zu programmieren. Zuerst haben wir uns eine grobe Grundidee (hier Hyperlink zur Grundidee) überlegt, die das Design unseres Spiels bestimmt. Außerdem haben wir uns überlegt, welche Gegenstände und Charaktere im Spiel vorkommen sollen. Zum Beispiel wollen wir natürlich einen Helden in unser Spiel integrieren. Damit es nicht zu einfach wird, braucht dieser noch Gegner, da die Welt radioaktiv ist, sind die Gegner verseucht. Die Gegenstände sollen Münzen und Flaschen mit Heilsaft sein. 
  Außerdem haben wir uns mit der Programmiersprache Python beschäftigt, da wir das Spiel entweder damit oder mit Greenfoot programmieren werden.
 <h2>2.Woche 2 (20.02. - 26.02.)</h2>
  
  Wir haben uns beide weiter mit der Thematik beschäftigt, diese Bestand aus dem Lesen von Büchern und dem Lernen aus dem Internet über YouTube und Co anschließend entschieden wir uns dafür, mit Phyton zu arbeiten. Wir haben uns für Phyton entschieden, da uns die Programmierstruktur logischer erschien und wir uns herausfordern wollten. In der nächsten Woche werden wir uns also tiefer in diese Programmiersprache einarbeiten, dies wird großteils in alleiniger Arbeit geschehen.
  
  <h2>3. Woche 3 (27.02. - 05.03.)</h2>
  Wie bereits angekündigt, haben sich alle mit Python beschäftigt, um einen relativ reibungslosen Arbeitsablauf zu gewährleisten. Dazu haben wir uns Anfängervideos angeschaut und Bücher über Python und Pygame gelesen, die uns den Einstieg erleichtern sollten. Obwohl wir wie in der letzten Woche alleine arbeiteten, sammelten und verglichen wir zwischendurch unsere Arbeitsergebnisse.
  
<h2>4. Woche 4 (06.03. - 12.03.)</h2>

Heute haben wir mit unserem Projekt begonnen. Dazu haben wir Python und die Pygame-Bibliothek sowie VSCode (zur Visualisierung unseres Codes) installiert. 
Wir haben angefangen, einen Bildschirm zu erstellen, auf dem unser Spiel später laufen wird. Außerdem haben wir einen Hintergrund erstellt, der die Farbe braun hat, passend zu unserem Spielthema, auf dem die Charaktere später laufen werden. Zuletzt haben wir die Geschwindigkeit unseres Spiels auf 60fps (frames per second) eingestellt.

<details><summary>Code</summary>
  
```python

 colour_surface = pygame.Surface((900,100)) #Boden im Hintergrund des Spiels 
 colour_surface.fill('burlywood4')           #Farbe des Bodens
colour_surface2 = pygame.Surface((900,20)) #Boden im Hintergrund des Spiels 2.Teil 
 colour_surface2.fill('burlywood3')           #Farbe des Bodens
 surface_himmel = pygame.Surface((900,580)) #Hintergrund des Spiels
 surface_himmel.fill('cornsilk3')            #Farbe des Hintergrundes 

```
  
  </details>
  
<h2> Seminartag 1 (05.04.)</h2>

Da Arvid leider krank war, habe ich, Alicia, alleine an dem Projekt weitergearbeitet. Um mir zu helfen, habe ich mir ein Video angeschaut, aus dem auch die Figur stammt. Außerdem habe ich den Code für uns umgeschrieben.

Ich habe angefangen, unseren Helden in das Spiel einzubauen. 

<details><summary>Code</summary>
  
```python

#Erstellung des characters (Figur, Position)
character = pygame.image.load('Bilder/character.png') #Installation eines Bildes für die Figur
character_rect = character.get_rect(topleft = (200,490)) #Erstellen eines Rechtecks zum besseren Bewegen der Figur
character_gravity = 0 #Erstellung der Schwerkraft-Variable

```

</details>

Zuerst wird die Figur auf unsere Oberfläche projiziert. Um später leichter damit arbeiten zu können, erstelle ich ein Rechteck und lege die Startposition fest. Die Position selbst wird sich im Laufe des Spiels natürlich noch ändern. 

Der nächste Schritt war, die Animation unseres Helden zu programmieren. Da wir am Ende ein Jump and Run Spiel erhalten möchten, sollte unsere Figur natürlich springen können, um später Hindernissen ausweichen zu können. 
Um das Springen animieren zu können brauchen wir erstmal Schwerkraft (gravity). Diese ist zum Beginn des Spiels gleich null. Damit sich die Schwerkraft in unserem Spiel auch bemerkbar macht, erhöht sich diese in jedem Durchlauf des Codes. Noch beeinflusst diese Schwerkraft unsere Figur aber nicht. Den Charachter kann man mit der Schwerkraft verbinden, indem wir unsere Figur, also genau genommen das Rechteck, nehmen und dieses mit der Schwerkraft gleichsetzen. Dies führt dazu, dass bei jedem Durchlauf des Spiels die Figur eine Position nach unten "fällt".

<details><summary>Code</summary>

```python

#Springbewegung der Figur
character_gravity += 1 #die Figur fällt 
character_rect.y += character_gravity #Verbindung der Figur mit der Schwerkraft
hindernis_rect.x += hindernis_left #Verbindung des Hindernises  mit der Bewegung nach links

```

</details>

Da unser Held jetzt allerdings ins Nichts fällt, habe ich noch einen Grund erstellt. Dieser ist bereits farblich hervorgehoben. Nun habe ich mit einer if clause gearbeitet. Wenn die Figur an einem bestimmten Punkt im Spiel ist, wird diese immer wieder auf eine gewisse Höhe zurück gesetzt. Nun fällt unser Spieler beim Starten des Spiels ebenfalls nicht mehr, da diese Höhe ebenfalls seine Grundposition ist. 

<details><summary>Code</summary>

```python

if character_rect.bottom >= 580: character_rect.bottom = 580 #ein Boden wird erstellt, damit die Figur nicht ins Nichts fällt

```
</details>

Um unsere Figur ebenfalls steuern zu können, habe ich Tastenfunktionen eingebaut. Mit einer kann man den Character springen lassen, mit anderen nach rechts und links steuern. Nun sieht es so aus, als würde unsere Figur springen.

<details><summary>Code</summary>

```python

keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:  #bei Tastendruck Sprung um 10 in die Höhe
  character_gravity = -10
elif keys[pygame.K_d]:  #bei Tastendruck um 1 nach rechts
  character_right = +1
elif keys[pygame.K_a]:  #bei Tastendruck um 1 nach links
  character_left = -1
  
```

</details>

Leider ist bei dem Schritt, dass man die Figur nach recht und links steuern kann, ein Problem aufgetreten. Ich habe diese Steuerung nach dem gleichen Prinzip wie mit der Schwerkaraft gemacht. Drückt man allerdings die entsprechende Taste für rechts, so läuft der Character kontinuierlich nach rechts und lässt sich nicht wirklich steuern, wie es bei dem Sprung der Falls ist. Drück man nun die Taste für links, bleibt die Figur stehen. Dies ist auch der Fall, drückt man erst die Taste, die nach links steuert. Die Sprungfunktion bleibt aber erhalten, die Figur kann ebenfalls während der Bewegung nach rachts oder links Sprünge ausführen.  Um das Problem zu lösen habe ich ein "elif" statt einses "if"s eingebaut, allerdings führte dies ebenfalls zu keiner Lösung. Da diese Figur sowieso nur zum Lernen gedacht war, ist dies nicht weiter schlimm, aber sehr schade. Bei einem Jump and Run Spiel kann die Figur nur springen und der Hintergrund bewegt sich quasi endlos, das heißt ich habe, zwar ungewollt, die Funktion für diesen endlosen Hintergrund erarbeitet.

<h2>Woche 5 (24.4. - 30.04.)</h2>

Diese Woche habe ich, Alicia, an dem Spiel weitergearbeitet und es um ein Hindernis erweitert. 
Zuerst habe ich ein passendes Bild ausgesucht. Da wir uns für ein apokalyptisches Thema entschieden haben, ist das Hindernis ein Fass mit radioaktivem Material. Die erste Schwierigkeit bestand darin, dass das Bild beim Start des Spiels nicht angezeigt wurde. Ich habe dann recherchiert, aber keinen Fehler in unserem Code gefunden. Also habe ich verschiedene Bilddateien ausprobiert, aber es gab keinen Unterschied. Schließlich bin ich selbst auf die Lösung gekommen. An einer anderen Stelle im Code muss noch einmal angegeben werden, an welcher Stelle im Spiel das Bild erscheinen soll, aber das hatte ich vergessen. Nachdem ich die Anweisung ergänzt hatte, wurde das Hindernis angezeigt, und ich habe das Bild an der vorgesehenen Stelle platziert und es, wie die Figur zuvor, in ein Rechteck verwandelt, um die Arbeit später zu erleichtern.

<details><summary>Code</summary>

```python

#Erstellung des Hindernises
hindernis = pygame.image.load('Bilder/hindernis.png') #Installation des Bildes für das Hindernis
hindernis_rect = hindernis.get_rect(topleft = (500,510 ))#Erstellen einses Rechtecks

```
In unserem "while True" Lopp müssen wir dann noch folgendes ergänzen:

```python

screen.blit(surface_himmel,(0,0)) #Himmel wird auf dem Display angezeigt

```
 
</details>

Zudem haben wir dieses Woche ebenfalls die Bewegung des Hindernises programmiert. Diese ist ähnlich aufgebaut, wie die Bewegung der Figur. Wir haben eine Variable erstellt und diese zuerst gelich null gesetzt. Später im Code haben wir diese Variable dann mit dem Hindenis verbunden und pro Loop um 5 erhöht.

<details><summary>Code</summary>

```python

hindernis_left = 0 #Erstellung der Bewegungs-Variable für das Hindernis

```

Im "while True" Loop:

```python

elif keys[pygame.K_a]:  #bei Tastendruck um 5 nach links
  hindernis_left = -5

 ```
 
</details>

<h2>Woche 6 (01.05. - 07.05.) </h2>

Diese Woche haben wir ein neues Problem beim Praxistest des Spiels gefunden. 
Dieses bestand darin, dass unser Hindernis nach dem Start des Spiels mit dem Boden verschmilzt, also eine rote Spur hinter sich herzieht, die nicht verschwindet. Um dieses Problem zu lösen, haben wir natürlich zuerst nach Fehlern in unserem Code gesucht, dort aber keinen Fehler gefunden. Dann haben wir im Internet recherchiert, aber auch so haben wir keinen Hinweis auf einen Fehler gefunden. Schließlich haben wir die Lösung selbst gefunden, das Problem bestand darin, dass wir zwei Farbblöcke für unseren Boden verwendet haben. Nachdem wir einen der Beiden entfernt hatten, bewegte sich unser Hindernis ohne Komplikationen. 

Außerdem haben wir mit der Programmierung unseres Scores angefangen. Der Score soll während des Spielens zu sehen sein und zählt die Sekunden, die der Spieler am Leben bleibt. In pygame gibt es dazu eine eingebaute Funktion, die die Zeit zählt.

<details><summary>Code</summary>

```python

def display_score():
    time = int(pygame.time.get_ticks() / 1000)  - start_time #Sekunden, die der Spieler am Leben bleibt
    score_surface = font.render(f'Score: {time}',False,(64,64,64)) #Scoreanzeige während des Spiels
    score_rect = score_surface.get_rect(center = (425,50)) #Formatierung zum Rechteck
    screen.blit(score_surface, score_rect) #Score wird nun auf dem Display angezeigt
    return time

start_time = 0 #Start des Scores

 ```
 
</details>

Leider wird der Score aber noch nicht auf dem Display angezeigt.

<h2>Woche 7 (08.05. - 14.05.)</h2>

Arvid hat an unserer Projektseite weitergearbeitet und die generelle Spielidee erläutert. Die Spielidee bestand aus 6 verschiedenen Aspekten, unsere Aufgabe war uns für jeden Bereich eine eigenerarbeitete Idee zu kreieren. Wir haben uns entschieden auf der Projektseite die Punkte: Spielname, Charaktere, Ziele, Hintergrund, Punkte und Steuerung festzuhalten. Außerdem teilten wir unser Projekt in 2 Phasen ein. 

Alicia hat versucht das Problem mit der Schrift zu lösen, welche auf dem Display nicht sichtbar ist. Dafür hat sie recherchiert und verschiedenen Schreibmethoden ausprobiert, allerdings hat sie den Fehler bisher nicht gefunden und der Fehler bleibt weiterhin bestehen. Es ist allerdings sicher, dass es kein Schreibfehler oder Funktionsfehler ist, da diese Fehlerarten beide vom Programm angezeigt werden würden, diese allerdings ausbleiben. Später ist dann jedoch aufgefallen, dass es zwar eine Funktion gitb, dass der Score angezeigt wird, diese allerdings nur in der definition Funktion ist. Die anderen Gegnstände und Figuren (z.B. Hintergrund, Figur) haben diese Funktion aber erst in dem While-True-Loop. Wir haben dort also eine weitere Funktion hinzugefügt, und der Score wurde endlich angezeigt.

<details><summary>Code</summary>

```python

display_score()

 ```
 
</details>

<h2>Seminartag 2 (17.05.)</h2>
Alicia war leider krank, daher musste ich, Arvid, alleine an unserem Projekt weiterarbeiten. <br>
In dieser Programmiereinheit haben ich mich darauf konzentriert, den Score besser in unser Jump and Run-Spiel zu integrieren. 

Ich habe eine Variable namens "score" erstellt, die den aktuellen Punktestand des Spielers anzeigt. 
Diese Variable wurde zu Beginn des Spiels auf 0 gesetzt. Diese Variable wurde mit der Scoreanzeige im While-True-Loop gleichgesetzt, damit sich diese fortlaufend aktualisiert.

<details><summary>Code</summary>

```python

score = display_score()

 ```
 
</details>

Ich habe das Jump and Run-Spiel getestet, um sicherzustellen, dass der Score korrekt berechnet und angezeigt wird. Dabei habe ich verschiedene Testfälle durchgespielt, um sicherzugehen, dass die Score-Berechnung für verschiedene Zeitwerte ordnungsgemäß funktioniert. <br>

Damit unser Spiel nicht nach einem Hindernis einfach beendet ist, wird dieses, sobald es einen bestimmten Punkt erreicht, auf einen neuen Punkt gesetzt, und erscheint so wieder im Spiel.

<details><summary>Code</summary>

```python

 if hindernis_rect.left <= -20: hindernis_rect.left = 920 #Hindernis wird immer wieder neu eingesetzt

 ```
 
</details>

Bisher passiert nichts, sobald sich unsere Firgur und das Hinerniss berühren. Wenn die Figur mit dem Hinderniss kollidiert soll der Spieler zu einem Endbildschirm weiter geführt werden, der rot ist. Am Anfang hatten wir das Problem, dass unser Endbildschrim nur angezeigt wurde, während der Kollision. Sobald unsere figur das Hindernis allerdings passiert hatte, konnte man normal weiterspielen. Um diesen Fehler zu beheben, haben wir uns erneut das YouTube Video angeguckt, mit dem wir auch zu begin gearbeitet hatten. In diesem Viedo wurde erklärt, dass man mit einer Variable "game active" arbeiten muss, damit der Endbildschirm dauerhaft angezeigt wird. Sollte die Figur mit dem Hindernis kollidieren, wird diese Variable auf "False" gesetzt und der Endbildschirm angezeigt.

<details><summary>Code</summary>
  
 ```python
  
         #Kollision
        if character_rect.colliderect(hindernis_rect): 
            game_active = False
    else:
        screen.fill('red')
        screen.blit(score_end,end_rect)  
  
  ``` 
</details>

<h2>Woche 8 (22.05.-28.05.)</h2>

Wie haben den finalen Namen für unser Spiel ausgesucht. Bisher hieß dieses "Rump and Jun". Dieser Name war allerdings zu einfallslos, daher haben wir beschlossen das Spiel "The Radiant Escape" zu nennen. Dieser Name bezieht sich sowohl auf die Art unseres Spiels als auch auf die Hintergrundgeschiechte mit der radioaktiv versäuchten Welt.

Außerdem haben wir die Springbewegung unserer Figur begrenzt, damit diese nach oben hin nicht über den Bildschrimrand hinausspringen kann.

<details><summary>Code</summary>

```python

 if character_rect.top <= 300: character_rect.top = 450 #Figur springt nicht über den Bildschirmrand hinaus

 ```
 
</details>

<h2>Woche 9 (29.05.- 04.06.)</h2>

Alicia hat an dem Game-over-Bildschirm weitergearbeitet. Bisher wurde dieser nur rot, sobald eine Kollision zwischen der Figur un dem Hinderniss stattfand. Jetzt zeigt er auch "Game over!" an.

 ```python
  
         #Kollision
        if character_rect.colliderect(hindernis_rect): 
            game_active = False
    else:
        screen.fill('red')
        screen.blit(score_end,end_rect)  
  
  ``` 

<details><summary>Endbildschirm</summary>
  
 ![image](https://github.com/aliceimwonderland/projekt/assets/111736084/ffc4b25e-3eb0-4137-b4d9-f80150df7551)
  
  </details>

<h2>Seminartag 3 (15.06.)</h2>

Wir haben uns heute hauptsächlich auf die Optimierung des Endbilschirms konzentriert. Ziel war es, dass der Score, welcher bereits während des Spielens angezeigt wird, auch auf dem Endbildschirm zu sehen ist. 
