---
title: Validieren Sie das gesamte Arbeitsblatt statt nur der aktualisierten Zellen
type: docs
weight: 80
url: /de/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
## **Mögliche Nutzungsszenarien**
Standardmäßig überprüft GridWeb nur die aktualisierten Zellen und nicht das gesamte Arbeitsblatt. Wenn Sie jedoch das gesamte Arbeitsblatt auf der Clientseite validieren möchten, bevor GridWeb eine Anfrage an den Server sendet, sollten Sie die Variable needValidateall in acwmain.js auf „true“ setzen.
## **Validieren Sie das gesamte Arbeitsblatt statt nur der aktualisierten Zellen**
Der folgende Screenshot zeigt die Variable needValidateall in acwmain.js. Bitte setzen Sie es auf true und GridWeb validiert jetzt Ihr gesamtes Arbeitsblatt, nicht nur die aktualisierten Zellen.

![todo: Bild_alt_Text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


