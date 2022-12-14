---
title: Averigüe si el proyecto VBA está protegido
type: docs
weight: 80
url: /es/java/find-out-if-vba-project-is-protected/
---
## **Posibles escenarios de uso**
 Puede averiguar si el proyecto VBA (Visual Basic Applications) de su archivo de Excel está protegido o no con Aspose.Cells usando[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)método
## **Código de muestra**
 El siguiente código de muestra crea un libro de trabajo y luego verifica si su proyecto VBA está protegido o no. Luego protege el proyecto de VBA y nuevamente verifica si su proyecto de VBA está protegido o no. Consulte su salida de consola para obtener una referencia. Antes de la protección,[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) devoluciones**falso** pero después de la protección, vuelve**verdadero**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Salida de consola**
Esta es la salida de la consola del código de muestra anterior para una referencia.

{{< highlight "java" >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
