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

 colour_surface = pygame.Surface((900,120)) #Boden im Hintergrund des Spiels 
 colour_surface.fill('burlywood4')           #Farbe des Bodens
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
character_rect = character.get_rect(topleft = (200,490)) #Erstellen eines Rechtecks zum besseren bewegen der Figur
character_gravity = 0 #Ausgangsposition der Figur

```

</details>

Zuerst wird die Figur auf unsere Oberfläche projiziert. Um später leichter damit arbeiten zu können, erstelle ich ein Rechteck und lege die Startposition fest. Die Position selbst wird sich im Laufe des Spiels natürlich noch ändern. 

Der nächste Schritt war, die Animation unseres Helden zu programmieren. Da wir am Ende ein Jump and Run Spiel erhalten möchten, sollte unsere Figur natürlich springen können, um später Hindernissen ausweichen zu können. 
Um das Springen animieren zu können brauchen wir erstmal Schwerkraft (gravity). Diese ist zum Beginn des Spiels gleich null. Damit sich die Schwerkraft in unserem Spiel auch bemerkbar macht, erhöht sich diese in jedem Durchlauf des Codes. Noch beeinflusst diese Schwerkraft unsere Figur aber nicht. Den Charachter kann man mit der Schwerkraft verbinden, indem wir unsere Figur, also genau genommen das Rechteck, nehmen und dieses mit der Schwerkraft gleichsetzen. Dies führt dazu, dass bei jedem Durchlauf des Spiels die Figur eine Position nach unten "fällt".

![image](https://user-images.githubusercontent.com/111736084/233837279-4c6138f2-6460-42a8-a74f-7399775bc958.png)


Da unser Held jetzt allerdings ins Nichts fällt, habe ich noch einen Grund erstellt. Dieser ist bereits farblich hervorgehoben. Nun habe ich mit einer if clause gearbeitet. Wenn die Figur an einem bestimmten Punkt im Spiel ist, wird er immer wieder auf eine gewisse Höhe zurück gesetzt. Nun fällt unser Spieler aber nicht mehr, da diese Höhe ebenfalls seine Grundposition ist. 

![image](https://user-images.githubusercontent.com/111736084/233837325-d3eda724-6aaa-4b5b-881f-5fdc5f7b5c10.png)


Um dieses Problem zu lösen, und die Figur ebendalls steuern zu können, habe ich Tastenfunktionen eingebaut. Mit einer kann man den Character springen lassen, mit anderen nach rechts und links steuern. Nun sieht es so aus, als würde unsere Figur springen.

![image](https://user-images.githubusercontent.com/111736084/233837348-5a2858b9-096c-4d67-a333-12354f2d686b.png)

Leider ist bei dem Schritt, dass man die Figur nach recht und links steuern kann, ein Problem aufgetreten. Ich habe diese Steuerung nach dem gleichen Prinzip wie mit der Schwerkaraft gemacht. Drückt man allerdings die entsprechende Taste für rechts, so läuft der Character kontinuierlich nach rechts und lässt sich nicht wirklich steuern, wie es bei dem Sprung der Falls ist. Drück man nun die Taste für links, bleibt die Figur stehen. Dies ist auch der Fall, drückt man erst die Taste, die nach links steuert. Die Sprungfunktion bleibt aber erhalten, die Figur kann ebenfalls während der Bewegung nach rachts oder links Sprünge ausführen.  Um das Problem zu lösen habe ich ein "elif" statt einses "if"s eingebaut, allerdings führte dies ebenfalls zu keiner Lösung. Da diese Figur sowieso nur zum Lernen gedacht war, ist dies nicht weiter schlimm, aber sehr schade. Bei einem Jump and Run Spiel kann die Figur nur springen und der Hintergrund bewegt sich quasi endlos, das heißt ich habe, zwar ungewollt, die Funktion für diesen endlosen Hintergrund erarbeitet.

<h2>Woche 5 (24.4. - 30.04.)</h2>

Heute habe ich, Alicia, an dem Spiel weitergearbeitet und es um ein Hindernis erweitert. 
Zuerst habe ich ein passendes Bild ausgesucht. Da wir uns für ein apokalyptisches Thema entschieden haben, ist das Hindernis ein Fass mit radioaktivem Material. Die erste Schwierigkeit bestand darin, dass das Bild beim Start des Spiels nicht angezeigt wurde. Ich habe dann recherchiert, aber keinen Fehler in unserem Code gefunden. Also habe ich verschiedene Bilddateien ausprobiert, aber es gab keinen Unterschied. Schließlich bin ich selbst auf die Lösung gekommen. An einer anderen Stelle im Code muss noch einmal angegeben werden, an welcher Stelle im Spiel das Bild erscheinen soll, aber das hatte ich vergessen. Nachdem ich die Anweisung ergänzt hatte, wurde das Hindernis angezeigt, und ich habe das Bild an der vorgesehenen Stelle platziert und es, wie die Figur zuvor, in ein Rechteck verwandelt, um die Arbeit später zu erleichtern.

<h2>Woche 6 (01.05. - 07.05.) </h2>

Diese Woche haben wir ein neues Problem beim Praxistest des Spiels gefunden. 
Dieses bestand darin, dass unser Hindernis nach dem Start des Spiels mit dem Boden verschmilzt, also eine rote Spur hinter sich herzieht, die nicht verschwindet. Um dieses Problem zu lösen, haben wir natürlich zuerst nach Fehlern in unserem Code gesucht, dort aber keinen Fehler gefunden. Dann haben wir im Internet recherchiert, aber auch so haben wir keinen Hinweis auf einen Fehler gefunden. Schließlich haben wir die Lösung selbst gefunden, das Problem bestand darin, dass wir zwei Farbblöcke für unseren Boden verwendet haben. Nachdem wir einen der Beiden entfernt hatten, bewegte sich unser Hindernis ohne Komplikationen. 

<h2>Woche 7 (08.05. - 14.05.)</h2>

Arvid hat an unserer Projektseite weitergearbeitet und die generelle Spielidee erläutert. Die Spielidee bestand aus 6 verschiedenen Aspekten, unsere Aufgabe war uns für jeden Bereich eine eigenerarbeitete Idee zu kreieren. Wir haben uns entschieden auf der Projektseite die Punkte: Spielname, Charaktere, Ziele, Hintergrund, Punkte und Steuerung festzuhalten. Außerdem teilten wir unser Projekt in 2 Phasen ein. 

Alicia hat versucht das Problem mit der Schrift zu lösen, welche auf dem Display nicht sichtbar ist. Dafür hat sie recherchiert und verschiedenen Schreibmethoden ausprobiert, allerdings hat sie den Fehler bisher nicht gefunden und der Fehler bleibt weiterhin bestehen. Es ist allerdings sicher, dass es kein Schreibfehler oder Funktionsfehler ist, da diese Fehlerarten beide vom Programm angezeigt werden würden, diese allerdings ausbleiben.

<h2>Seminartag 2 (17.05.)</h2>
Alicia war leider krank, daher musste ich, Arvid, alleine an unserem Projekt weiterarbeiten. <br>
In dieser Programmiereinheit haben ich mich darauf konzentriert, einen Score in unser Jump and Run-Spiel zu integrieren. Der Score soll die Leistung des Spielers widerspiegeln und basiert auf der gemessenen Zeit, die der Spieler benötigt, um das Level abzuschließen. 
Initialisierung der Score-Variablen: <br>
Wir haben eine Variable namens "score" erstellt, die den aktuellen Punktestand des Spielers speichert. 
Diese Variable wurde zu Beginn des Spiels auf 0 gesetzt. Integration der Zeiterfassung: Wir haben die notwendigen Codeänderungen vorgenommen, um die Zeitmessung beim Start des Levels zu starten und beim Abschluss zu beenden. <br>
Dazu haben wir den Pygame-eigenen Timer verwendet, um die vergangene Zeit in Millisekunden zu erfassen. Beim Start des Levels haben wir die Zeitmessung gestartet und den Wert in einer Variable namens "start_time" gespeichert. <br>
Beim Abschluss des Levels haben wir die Zeitmessung beendet und den Wert in einer Variable namens "end_time" gespeichert. 
Anzeige des Scores: <br>
Wir haben eine Funktion namens "draw_score" erstellt, um den Score auf dem Bildschirm anzuzeigen. 
Diese Funktion verwendet die Pygame-Funktionalitäten, um Text auf dem Bildschirm zu zeichnen. Der aktuelle Scorewert wird in einem speziellen Score-Bereich auf dem Bildschirm angezeigt. 
Aktualisierung des Scores während des Spiels: <br>
Wir haben die Score-Anzeige so aktualisiert, dass sie während des Spiels fortlaufend den aktuellen Scorewert darstellt. Dazu haben wir die Funktion "draw_score" in der Haupt-Update-Schleife des Spiels aufgerufen. 
Abschlussarbeiten: <br>
Wir haben das Jump and Run-Spiel getestet, um sicherzustellen, dass der Score korrekt berechnet und angezeigt wird. Dabei haben wir verschiedene Testfälle durchgespielt, um sicherzugehen, dass die Score-Berechnung für verschiedene Zeitwerte ordnungsgemäß funktioniert. <br>
Gegebenenfalls haben wir einige kleine Fehler behoben und Optimierungen vorgenommen, um sicherzustellen, dass der Score einwandfrei funktioniert. <br>
Fazit: In dieser Programmiereinheit haben wir erfolgreich den Score in unser Jump and Run-Spiel integriert. Durch die Nutzung der Pygame-Bibliothek konnten wir die gemessene Zeit verwenden, um den Score zu berechnen.


<h2>Woche 8 (22.05.-28.05.)</h2>

Wie haben den finalen Namen für unser Spiel ausgesucht. Bisher hieß dieses "Rump and Jun". Dieser Name war allerdings zu einfallslos, daher haben wir beschlossen das Spiel "The Radiant Escape" zu nennen. Dieser Name bezieht sich sowohl auf die Art unseres Spiels als auch auf die Hintergrundgeschiechte mit der radioaktiv versäuchten Welt.

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
