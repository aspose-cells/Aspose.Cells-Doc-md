---
title: Ausführen der clientseitigen Funktion beim Wechsel der GridWeb-Seite
type: docs
weight: 140
url: /de/net/execute-client-side-function-on-gridweb-page-change/
---
## **Mögliche Nutzungsszenarien**
Manchmal müssen Sie Ihre clientseitige Funktion ausführen, wenn sich die GridWeb-Seite ändert. Aspose.Cells.GridWeb stellt hierfür die Eigenschaft OnPageChangeClientFunction zur Verfügung. Bitte legen Sie diese Eigenschaft mit der clientseitigen Funktion fest, die Sie ausführen möchten.
## **Ausführen der clientseitigen Funktion beim Wechsel der GridWeb-Seite**
Das folgende aspx-Markup erläutert, wie die OnPageChangeClientFunction-Eigenschaft verwendet wird. Es setzt die Eigenschaft mit der clientseitigen Funktion namens MyOnPageChange. Bitte beachten Sie, dass diese Eigenschaft nur gültig ist, wenn Sie Paging aktiviert haben, dh EnablePaging="true". Wenn Sie jetzt die GridWeb-Seite ändern, wird die clientseitige Funktion MyOnPageChange aufgerufen, die die ausgibt**aktueller Seitenindex** auf der**Konsole** wie in diesem Screenshot gezeigt.

![todo: Bild_alt_Text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Beispielcode**
Dies ist der Code der clientseitigen Funktion MyOnPageChange, die aufgrund der Einstellung der OnPageChangeClientFunction ="MyOnPageChange"-Eigenschaft in GridWeb ausgeführt wird. Dies ist das vollständige Aspx-Seiten-Markup.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
