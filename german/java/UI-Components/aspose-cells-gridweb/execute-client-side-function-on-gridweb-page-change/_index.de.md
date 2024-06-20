---
title: Ausführen der Client seitigen Funktion bei Änderung der GridWeb Seite
type: docs
weight: 70
url: /de/java/execute-client-side-function-on-gridweb-page-change/
---

## **Mögliche Verwendungsszenarien**
Manchmal müssen Sie Ihre Client-seitige Funktion ausführen, wenn sich die GridWeb-Seite ändert. Aspose.Cells.GridWeb bietet die OnPageChangeClientFunction-Eigenschaft zu diesem Zweck. Bitte setzen Sie diese Eigenschaft mit der Client-seitigen Funktion, die Sie ausführen möchten.
## **Ausführen der Client-seitigen Funktion bei Änderung der GridWeb-Seite**
Der folgende Java-Code erklärt, wie die GridWebBean.setOnPageChangeClientFunction() Eigenschaft genutzt wird. Es setzt die Eigenschaft mit der clientseitigen Funktion namens MyOnPageChange. Bitte beachten Sie, dass diese Eigenschaft nur gültig ist, wenn Sie das Paging aktiviert haben, d.h. GridWebBean.setEnablePaging(true). Jetzt, jedes Mal, wenn Sie die GridWeb-Seite ändern, wird die clientseitige Funktion MyOnPageChange aufgerufen, die den **aktuellen Seitenindex** in der **Konsole** ausgibt, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Beispielcode**
Dies ist der Code der clientseitigen Funktion MyOnPageChange, die ausgeführt wird, weil dieser Befehl verwendet wird: Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Der folgende Code erklärt, wie das Paging aktiviert und die OnPageChangeClientFunction-Eigenschaft gesetzt wird.

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
