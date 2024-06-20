---
title: Descubrir si el Proyecto VBA está Protegido
type: docs
weight: 20
url: /es/net/find-out-if-vba-project-is-protected/
---

## **Descubra si el Proyecto VBA está protegido en C#**

Puede averiguar si el Proyecto de Visual Basic Applications (VBA) de su archivo de Excel está protegido o no con Aspose.Cells usando la propiedad [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected).

## **Código de muestra**

El siguiente código de muestra crea un libro de trabajo y luego verifica si su proyecto de VBA está protegido o no. Luego protege el proyecto de VBA y nuevamente verifica si su proyecto de VBA está protegido o no. Consulte su salida por consola como referencia. Antes de la protección, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) devuelve **falso**, pero después de la protección, devuelve **verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **Salida de la consola**

Esta es la salida en consola del código de muestra anterior como referencia.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
