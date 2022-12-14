---
title: Averigüe si el proyecto VBA está protegido
type: docs
weight: 20
url: /es/net/find-out-if-vba-project-is-protected/
---
## **Averigüe si el proyecto VBA está protegido en C#**

 Puede averiguar si el proyecto VBA (Visual Basic Applications) de su archivo de Excel está protegido o no con Aspose.Cells usando[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected)propiedad.

## **Código de muestra**

 El siguiente código de muestra crea un libro de trabajo y luego verifica si su proyecto VBA está protegido o no. Luego protege el proyecto de VBA y nuevamente verifica si su proyecto de VBA está protegido o no. Consulte su salida de consola para obtener una referencia. Antes de la protección,[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) devoluciones**falso** pero después de la protección, vuelve**verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **Salida de consola**

Esta es la salida de la consola del código de muestra anterior para una referencia.

{{< highlight "java" >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
