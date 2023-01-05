---
title: Ausführen der clientseitigen Funktion beim Wechsel der GridWeb-Seite
type: docs
weight: 70
url: /de/java/execute-client-side-function-on-gridweb-page-change/
---
## **Mögliche Nutzungsszenarien**
Manchmal müssen Sie Ihre clientseitige Funktion ausführen, wenn sich die GridWeb-Seite ändert. Aspose.Cells.GridWeb stellt hierfür die Eigenschaft OnPageChangeClientFunction zur Verfügung. Bitte legen Sie diese Eigenschaft mit der clientseitigen Funktion fest, die Sie ausführen möchten.
## **Ausführen der clientseitigen Funktion beim Wechsel der GridWeb-Seite**
Der folgende Java-Code erläutert, wie Sie die Eigenschaft GridWebBean.setOnPageChangeClientFunction() verwenden. Es setzt die Eigenschaft mit der clientseitigen Funktion namens MyOnPageChange. Bitte beachten Sie, dass diese Eigenschaft nur gültig ist, wenn Sie Paging aktiviert haben, dh GridWebBean.setEnablePaging(true). Wenn Sie jetzt die GridWeb-Seite ändern, wird die clientseitige Funktion MyOnPageChange aufgerufen, die die ausgibt**aktueller Seitenindex** auf der**Konsole** wie in diesem Screenshot gezeigt.

![todo: Bild_alt_Text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Beispielcode**
Dies ist der Code der clientseitigen Funktion MyOnPageChange, die aufgrund dieser Zeile ausgeführt wird, dh Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Der folgende Code erläutert, wie Paging aktiviert und die OnPageChangeClientFunction-Eigenschaft festgelegt wird.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
