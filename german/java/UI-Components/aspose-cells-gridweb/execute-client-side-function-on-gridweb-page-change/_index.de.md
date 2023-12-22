---
title: Führen Sie eine clientseitige Funktion bei einer GridWeb-Seitenänderung aus
type: docs
weight: 70
url: /de/java/execute-client-side-function-on-gridweb-page-change/
---
##  **Mögliche Nutzungsszenarien**
Manchmal müssen Sie Ihre clientseitige Funktion ausführen, wenn sich die GridWeb-Seite ändert. Aspose.Cells.GridWeb stellt hierfür die Eigenschaft OnPageChangeClientFunction zur Verfügung. Bitte legen Sie diese Eigenschaft mit der clientseitigen Funktion fest, die Sie ausführen möchten.
##  **Führen Sie eine clientseitige Funktion bei einer GridWeb-Seitenänderung aus**
 Der folgende Java-Code erläutert, wie die Eigenschaft GridWebBean.setOnPageChangeClientFunction() verwendet wird. Es legt die Eigenschaft mit der clientseitigen Funktion namens MyOnPageChange fest. Bitte beachten Sie, dass diese Eigenschaft nur gültig ist, wenn Sie Paging aktiviert haben, also GridWebBean.setEnablePaging(true). Wenn Sie nun die GridWeb-Seite ändern, wird die clientseitige Funktion MyOnPageChange aufgerufen, die die ausgibt**Aktueller Seitenindex** auf der**Konsole** wie in diesem Screenshot gezeigt.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
##  **Beispielcode**
Dies ist der Code der clientseitigen Funktion MyOnPageChange, die aufgrund dieser Zeile ausgeführt wird, z. B. Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Im folgenden Code wird erläutert, wie Paging aktiviert und die OnPageChangeClientFunction-Eigenschaft festgelegt wird.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
