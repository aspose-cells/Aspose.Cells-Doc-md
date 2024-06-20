---
title: Ausführen der Client seitigen Funktion bei Änderung der GridWeb Seite
type: docs
weight: 140
url: /de/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: Dieser Artikel erläutert, wie Sie mit Client JS Funktionen in GridWeb arbeiten.
---

## **Mögliche Verwendungsszenarien**
Manchmal müssen Sie Ihre Client-seitige Funktion ausführen, wenn sich die GridWeb-Seite ändert. Aspose.Cells.GridWeb bietet die OnPageChangeClientFunction-Eigenschaft zu diesem Zweck. Bitte setzen Sie diese Eigenschaft mit der Client-seitigen Funktion, die Sie ausführen möchten.
## **Ausführen der Client-seitigen Funktion bei Änderung der GridWeb-Seite**
Der folgende ASPX-Markup erklärt, wie die Eigenschaft OnPageChangeClientFunction verwendet wird. Sie setzt die Eigenschaft mit der Clientside-Funktion MyOnPageChange. Bitte beachten Sie, dass diese Eigenschaft nur gültig ist, wenn Sie das Paging aktiviert haben, d.h. EnablePaging="true". Wenn Sie nun die GridWeb-Seite ändern, wird die Clientside-Funktion MyOnPageChange aufgerufen, die den **aktuellen Seitenindex** in der **Konsole** ausgibt, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Beispielcode**
Dies ist der Code der Clientside-Funktion MyOnPageChange, der ausgeführt wird, weil die Eigenschaft OnPageChangeClientFunction="MyOnPageChange" in GridWeb gesetzt ist. Dies ist der komplette ASPX-Seitenmarkup.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
