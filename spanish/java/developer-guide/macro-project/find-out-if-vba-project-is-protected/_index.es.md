---
title: Descubrir si el Proyecto VBA está Protegido
type: docs
weight: 80
url: /es/java/find-out-if-vba-project-is-protected/
---

## **Escenarios de uso posibles**
Puede verificar si el Proyecto VBA (Visual Basic Applications) de su archivo de Excel está protegido o no con Aspose.Cells utilizando el método [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)
## **Código de muestra**
El siguiente código de muestra crea un libro de trabajo y luego verifica si su proyecto VBA está protegido o no. Luego protege el proyecto VBA y verifica nuevamente si su proyecto VBA está protegido o no. Por favor, consulte la salida en consola como referencia. Antes de la protección, [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) devuelve **false** pero después de la protección, devuelve **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Salida de la consola**
Esta es la salida en consola del código de muestra anterior como referencia.

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
