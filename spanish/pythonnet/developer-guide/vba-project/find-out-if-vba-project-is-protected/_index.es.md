---
title: Descubrir si el Proyecto VBA está Protegido
type: docs
weight: 20
url: /es/python-net/find-out-if-vba-project-is-protected/
---

## **Descubre si el proyecto VBA está protegido en Python**

Puedes determinar si el proyecto VBA (Visual Basic for Applications) de tu archivo de Excel está protegido o no usando Aspose.Cells para Python via .NET mediante la propiedad [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected).

## **Código de muestra**

El siguiente código de muestra crea un libro de trabajo y luego verifica si su proyecto de VBA está protegido o no. Luego protege el proyecto de VBA y nuevamente verifica si su proyecto de VBA está protegido o no. Consulte su salida por consola como referencia. Antes de la protección, [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected) devuelve **falso**, pero después de la protección, devuelve **verdadero**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FindoutifVBAProjectisProtected.py" >}}

## **Salida de la consola**

Esta es la salida en consola del código de muestra anterior como referencia.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}

