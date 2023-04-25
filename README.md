# Rump and Jun

<h2>1. Stunde (14.02.2023)</h2>

  
  Wir haben unsere Projektidee konkretisiert. Wir haben beschlossen, ein Platform Game bzw. ein Jump-and-Run Game zu programmieren. Zuerst haben wir uns eine grobe Hintergrund (hier Hyperlink zur Hintergrundidee) Idee überlegt, welche das Design unseres Spiels bestimmt. Weiterhin haben wir über weitere Items und Charaktere im Spiel nachgedacht. Zum Beispiel wollen wir natürlich einen Helden in unser Spiel integrieren. Damit es nicht zu einfach wird, braucht dieser noch Gegenspieler, da die Welt Radioaktiv ist, sind die Gegner verseucht. Die Items sollen Münzen und Flaschen mit Heilsaft sein.
  Außerdem haben wir uns mit der Programmiersprache Python außeinandergesetzt, da wir entweder mit dieser oder mit Greenfoot das Spiel programmieren werden.
  
 <h2>2.Woche (20.02.-26.02.)</h2>
  
  Wir haben uns beide weiter mit der Thematik beschäftigt und anschließend entschieden, mit Phyton zu arbeiten. Wir haben uns für Phyton entschieden, da uns die Programmierstruktur logischer erschien und wir uns herausfordern wollten. Die nächste Woche werden wir uns also in diese Programmiersprache einarbeiten.
  
  <h2>3. Woche (27.02.-05.03.)</h2>
  Jeder hat sich mit Python bschäftigt, um einen relativ reibungslosen Arbeitsablauf zu garantieren. Hierzu haben wir Einsteiger Videos geguckt und in Büchern gelesen, die den Anang erleichtern sollen.
  
<h2>4. Woche (06.03.-12.03.)</h2>

Heute haben wir unser Projekt gestartet. Dazu haben wir Python und die Library Pygame sowie VSCode (für die Visualisierung unseres Codes) installiert. 
Wir haben damit begonnen ein Display zu erstellen, in diesem wird unser Spiel nachher laufen. Außerdem haben wir einen Untergrund erstellt, der die Farbe braun hat, passen zu unserer Spielthematik, auf dem die Characktere später laufen werden. Als letztes haben wir noch die Geschwindigkeit unseres Spiels auf 60fps (frames per second) festgelget.

<h3>Seminartag (05.04.)</h3>

Arvid war leider krank, daher habe ich, Alicia, alleine am Projekt weitergearbeitet. Zur Hilfe habe ich mir ein Video angeguckt, aus diesem stammt auch die Figur, und den Code für unseren Nutzen umgewandelt.

Ich habe damit begonnen, unseren Heldencharakter in das Spiel einzubauen. Diese ist eine Figur aus dem Internet. 

![image](https://user-images.githubusercontent.com/111736084/233835663-19765f3c-5403-44cc-8d7f-1e1ffc6ab41c.png)

Als erstes wird die Figur installiert. Um später das Arbeiten mit dieser einfacher zu gestalten, erstelle ich ein Rechteck und lege anschließend die Startposition fest. Die Position an sich wird sich im Verlauf des Spiels natürlich immer wieder ändern. 

Der nächste Schritt war, die Animation unseres Helden zu programmieren. Da wir am Ende ein Jump and Run Spiel erhalten möchten, sollte unsere Figur natürlich springen können, um später Hindernissen ausweichen zu können. 
Um das Springen animieren zu können brauchen wir erstmal Schwerkraft (gravity). Diese ist zum Beginn des Spiels gleich null. Damit sich die Schwerkraft in unserem Spiel auch bemerkbar macht, erhöht sich diese in jedem Durchlauf des Codes. Noch beeinflusst diese Schwerkraft unsere Figur aber nicht. Den Charachter kann man mit der Schwerkraft verbinden, indem wir unsere Figur, also genau genommen das Rechteck, nehmen und dieses mit der Schwerkraft gleichsetzen. Dies führt dazu, dass bei jedem Durchlauf des Spiels die Figur eine Position nach unten "fällt".

![image](https://user-images.githubusercontent.com/111736084/233837279-4c6138f2-6460-42a8-a74f-7399775bc958.png)


Da unser Held jetzt allerdings ins Nichts fällt, habe ich noch einen Grund erstellt. Dieser ist bereits farblich hervorgehoben. Nun habe ich mit einer if clause gearbeitet. Wenn die Figur an einem bestimmten Punkt im Spiel ist, wird er immer wieder auf eine gewisse Höhe zurück gesetzt. Nun fällt unser Spieler aber nicht mehr, da diese Höhe ebenfalls seine Grundposition ist. 

![image](https://user-images.githubusercontent.com/111736084/233837325-d3eda724-6aaa-4b5b-881f-5fdc5f7b5c10.png)


Um dieses Problem zu lösen, und die Figur ebendalls steuern zu können, habe ich Tastenfunktionen eingebaut. Mit einer kann man den Character springen lassen, mit anderen nach rechts und links steuern. Nun sieht es so aus, als würde unsere Figur springen.

![image](https://user-images.githubusercontent.com/111736084/233837348-5a2858b9-096c-4d67-a333-12354f2d686b.png)

Leider ist bei dem Schritt, dass man die Figur nach recht und links steuern kann, ein Problem aufgetreten. Ich habe diese Steuerung nach dem gleichen Prinzip wie mit der Schwerkaraft gemacht. Drückt man allerdings die entsprechende Taste für rechts, so läuft der Character kontinuierlich nach rechts und lässt sich nicht wirklich steuern, wie es bei dem Sprung der Falls ist. Drück man nun die Taste für links, bleibt die Figur stehen. Dies ist auch der Fall, drückt man erst die Taste, die nach links steuert. Die Sprungfunktion bleibt aber erhalten, die Figur kann ebenfalls während der Bewegung nach rachts oder links Sprünge ausführen.  Um das Problem zu lösen habe ich ein "elif" statt einses "if"s eingebaut, allerdings führte dies ebenfalls zu keiner Lösung. Da dieses Fiture sowieso nur zum Lernen gedacht war, ist dies nicht wieter schlimm aber sehr schade. Bei einem Jump and Run Spiel kann die Figur nur springen und der Hintergrund bewegt sich quasi endlos, das heißt ich habe, zwar ungewollt, die Funktion für diesen endlosen Hintergrund erarbeitet.

<h3>25.4.</h3>

Heute habe ich, Alicia, weiter am Spiel gearbeitet und es mit einem Hinderniss erweitert. Als erstes hat sie ein passendes Bild herausgesucht. Da wir uns für ein apokalyptisches Thema entschieden haben, ist das Hinderniss ein Fass, welches radioaktives Material enthält. Die erste Schwierigkeit bestand darin, dass das Bild nicht beim Starten des Spiels nicht angezeigt wurde. Darufhin habe ich recherchiert, doch keinen Fehler in unserem Code entdeckt. Also habe ich verschiedene Bilddateien ausprobiert, es hat aber keinen Unterschied ergeben. Schließlich bin ich am Ende selbst auf die Lösung gekommen. An einer weiteren Stelle im Code muss erneut angegeben werden, an welcher Stelle im Spiel das Bild erscheinen soll, dies hatte ich allerdings vergessen. Nachdem ich den Befehl ergänzt hatte, wurde das Hinderniss angezeigt.Anschließend habe ich das Bild an der vorgesehenen Stelle platziert und es, wie auch die Figur zuvor, zu einem rechteck umgeformt, damit die Arbeit später einfacher ist.

