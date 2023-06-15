# Radiant Escape Stundenprotokoll

<h2>Woche 1 (13.02. - 19.02.)</h2>

  
  Wir konkretisierten unsere Projektidee. Wir haben uns entschieden, ein Jump'n'Run Spiel zu programmieren. Zuerst haben wir uns eine grobe Grundidee (hier Hyperlink zur Grundidee) überlegt, die das Design unseres Spiels bestimmt. Außerdem haben wir uns überlegt, welche Gegenstände und Charaktere im Spiel vorkommen sollen. Zum Beispiel wollen wir natürlich einen Helden in unser Spiel integrieren. Damit es nicht zu einfach wird, braucht dieser noch Gegner, da die Welt radioaktiv ist, sind die Gegner verseucht. Die Gegenstände sollen Münzen und Flaschen mit Heilsaft sein. 
  Außerdem haben wir uns mit der Programmiersprache Python beschäftigt, da wir das Spiel entweder damit oder mit Greenfoot programmieren werden.
 <h2>2.Woche 2 (20.02. - 26.02.)</h2>
  
  Wir haben uns beide weiter mit der Thematik beschäftigt, diese Bestand aus dem Lesen von Büchern und dem Lernen aus dem Internet über YouTube und Co anschließend entschieden wir uns dafür, mit Phyton zu arbeiten. Wir haben uns für Phyton entschieden, da uns die Programmierstruktur logischer erschien und wir uns herausfordern wollten. Die nächste Woche werden wir uns also tiefer in diese Programmiersprache einarbeiten, dies geschieht großteils in alleiniger Arbeit.
  
  <h2>3. Woche 3 (27.02. - 05.03.)</h2>
  Jeder hat sich wie bereits angekündigt mit Python bschäftigt, um einen relativ reibungslosen Arbeitsablauf zu garantieren. Hierzu haben wir Einsteiger Videos geguckt und in Büchern zu Python und Pygame gelesen, die den Angang erleichtern sollten. Obwohl die Arbeit wie in der letzten Woche alleine stattfand, haben wir zwischendurch unsere Arbeitsergebnisse zusammengetragen und verglichen.
  
<h2>4. Woche 4 (06.03. - 12.03.)</h2>

Heute haben wir unser Projekt gestartet. Dazu haben wir Python und die Library Pygame sowie VSCode (für die Visualisierung unseres Codes) installiert. 
Wir haben damit begonnen ein Display zu erstellen, in diesem wird unser Spiel nachher laufen. Außerdem haben wir einen Untergrund erstellt, der die Farbe braun hat, passen zu unserer Spielthematik, auf dem die Characktere später laufen werden. Als letztes haben wir noch die Geschwindigkeit unseres Spiels auf 60fps (frames per second) festgelget.

<h2> Seminartag 1 (05.04.)</h2>

Arvid war leider krank, daher habe ich, Alicia, alleine am Projekt weitergearbeitet. Zur Hilfe habe ich mir ein Video angeguckt, aus diesem stammt auch die Figur. Außerdem habe ich den Code für unseren Nutzen umgewandelt.

Ich habe damit begonnen, unseren Heldencharakter in das Spiel einzubauen. Diese ist eine Figur aus dem Internet. 

![image](https://user-images.githubusercontent.com/111736084/233835663-19765f3c-5403-44cc-8d7f-1e1ffc6ab41c.png)

Als erstes wird die Figur auf unserem Surface projeziert. Um später das Arbeiten mit dieser einfacher zu gestalten, erstelle ich ein Rechteck und lege anschließend die Startposition fest. Die Position an sich wird sich im Verlauf des Spiels natürlich immer wieder ändern. 

Der nächste Schritt war, die Animation unseres Helden zu programmieren. Da wir am Ende ein Jump and Run Spiel erhalten möchten, sollte unsere Figur natürlich springen können, um später Hindernissen ausweichen zu können. 
Um das Springen animieren zu können brauchen wir erstmal Schwerkraft (gravity). Diese ist zum Beginn des Spiels gleich null. Damit sich die Schwerkraft in unserem Spiel auch bemerkbar macht, erhöht sich diese in jedem Durchlauf des Codes. Noch beeinflusst diese Schwerkraft unsere Figur aber nicht. Den Charachter kann man mit der Schwerkraft verbinden, indem wir unsere Figur, also genau genommen das Rechteck, nehmen und dieses mit der Schwerkraft gleichsetzen. Dies führt dazu, dass bei jedem Durchlauf des Spiels die Figur eine Position nach unten "fällt".

![image](https://user-images.githubusercontent.com/111736084/233837279-4c6138f2-6460-42a8-a74f-7399775bc958.png)


Da unser Held jetzt allerdings ins Nichts fällt, habe ich noch einen Grund erstellt. Dieser ist bereits farblich hervorgehoben. Nun habe ich mit einer if clause gearbeitet. Wenn die Figur an einem bestimmten Punkt im Spiel ist, wird er immer wieder auf eine gewisse Höhe zurück gesetzt. Nun fällt unser Spieler aber nicht mehr, da diese Höhe ebenfalls seine Grundposition ist. 

![image](https://user-images.githubusercontent.com/111736084/233837325-d3eda724-6aaa-4b5b-881f-5fdc5f7b5c10.png)


Um dieses Problem zu lösen, und die Figur ebendalls steuern zu können, habe ich Tastenfunktionen eingebaut. Mit einer kann man den Character springen lassen, mit anderen nach rechts und links steuern. Nun sieht es so aus, als würde unsere Figur springen.

![image](https://user-images.githubusercontent.com/111736084/233837348-5a2858b9-096c-4d67-a333-12354f2d686b.png)

Leider ist bei dem Schritt, dass man die Figur nach recht und links steuern kann, ein Problem aufgetreten. Ich habe diese Steuerung nach dem gleichen Prinzip wie mit der Schwerkaraft gemacht. Drückt man allerdings die entsprechende Taste für rechts, so läuft der Character kontinuierlich nach rechts und lässt sich nicht wirklich steuern, wie es bei dem Sprung der Falls ist. Drück man nun die Taste für links, bleibt die Figur stehen. Dies ist auch der Fall, drückt man erst die Taste, die nach links steuert. Die Sprungfunktion bleibt aber erhalten, die Figur kann ebenfalls während der Bewegung nach rachts oder links Sprünge ausführen.  Um das Problem zu lösen habe ich ein "elif" statt einses "if"s eingebaut, allerdings führte dies ebenfalls zu keiner Lösung. Da dieses Fiture sowieso nur zum Lernen gedacht war, ist dies nicht wieter schlimm aber sehr schade. Bei einem Jump and Run Spiel kann die Figur nur springen und der Hintergrund bewegt sich quasi endlos, das heißt ich habe, zwar ungewollt, die Funktion für diesen endlosen Hintergrund erarbeitet.

<h2>Woche 5 (24.4. - 30.04.)</h2>

Heute habe ich, Alicia, weiter am Spiel gearbeitet und es mit einem Hinderniss erweitert. Als erstes hat sie ein passendes Bild herausgesucht. Da wir uns für ein apokalyptisches Thema entschieden haben, ist das Hinderniss ein Fass, welches radioaktives Material enthält. Die erste Schwierigkeit bestand darin, dass das Bild nicht beim Starten des Spiels nicht angezeigt wurde. Darufhin habe ich recherchiert, doch keinen Fehler in unserem Code entdeckt. Also habe ich verschiedene Bilddateien ausprobiert, es hat aber keinen Unterschied ergeben. Schließlich bin ich am Ende selbst auf die Lösung gekommen. An einer weiteren Stelle im Code muss erneut angegeben werden, an welcher Stelle im Spiel das Bild erscheinen soll, dies hatte ich allerdings vergessen. Nachdem ich den Befehl ergänzt hatte, wurde das Hinderniss angezeigt.Anschließend habe ich das Bild an der vorgesehenen Stelle platziert und es, wie auch die Figur zuvor, zu einem rechteck umgeformt, damit die Arbeit später einfacher ist.

<h2>Woche 6 (01.05. - 07.05.) </h2>

<h2>Woche 7 (08.05. - 14.05.)</h2>

Arvid hat an unserer Projektseite weitergearbeitet und die generelle Spielidee erläutert.

Alicia hat versucht, dass Problem mit der Schrift zu lösen, welche auf dem Display nicht sichtbar ist. Dafür hat sie recherchiert und verschiedenen Schreibmethoden ausprobiert, allerdings hat sie den Fehler bisher nicht gefunden und der Fehler bleibt weiterhin bestehen. Es ist allerdings sicher, dass es kein Schreibfehler oder Funktionsfehler ist, da diese Fehlerarten beide vom Programm angezeigt werden würden, diese allerdings ausbleiben.

<h2>Seminartag 2 (17.05.)</h2>

<h2>Woche 8 (22.05.-28.05.)</h2>

Wie haben den finalen Namen für unser Spiel ausgesucht. Bisher hieß dieses "Rump and Jun". Dieser Name war allerdings zu einfallslos, daher haben wir beschlossen das Spiel "The Radiant Escape" zu nennen. Dieser Name bezieht sich sowohl auf die Art unseres Spiels als auch auf die Hintergrundgeschiechte mit der radiaktiv versäuchten Welt.

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


