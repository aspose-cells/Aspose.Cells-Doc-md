---
title: Gesamtes Arbeitsblatt validieren, anstatt nur der aktualisierten Zellen
type: docs
weight: 80
url: /de/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **Mögliche Verwendungsszenarien**
Standardmäßig validiert GridWeb nur die aktualisierten Zellen und nicht das gesamte Arbeitsblatt. Wenn Sie jedoch das gesamte Arbeitsblatt auf der Clientseite validieren möchten, bevor GridWeb eine Anfrage an den Server sendet, sollten Sie die Variable needValidateall in der acwmain.js auf true setzen.
## **Gesamtes Arbeitsblatt validieren, anstatt nur der aktualisierten Zellen**
Im folgenden Screenshot wird die needValidateall-Variable in acwmain.js angezeigt. Bitte setzen Sie sie auf true, und jetzt validiert GridWeb Ihr gesamtes Arbeitsblatt und nicht nur die aktualisierten Zellen.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


