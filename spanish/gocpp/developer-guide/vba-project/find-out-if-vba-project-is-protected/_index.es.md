---  
title: Averiguar si el proyecto VBA está protegido con Golang mediante C++  
linktitle: Descubrir si el Proyecto VBA está Protegido  
type: docs  
weight: 20  
url: /es/go-cpp/find-out-if-vba-project-is-protected/  
description: Verifique si el proyecto VBA de un archivo de Excel está protegido usando Aspose.Cells con Golang mediante C++  
---  

## **Descubra si el Proyecto VBA está protegido en C++**

Puede verificar si el proyecto VBA (Visual Basic for Applications) de su archivo de Excel está protegido o no usando Aspose.Cells y la propiedad [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/).

## **Código de muestra**

El siguiente código de muestra crea un libro de trabajo y luego verifica si su proyecto VBA está protegido o no. Luego protege el proyecto VBA y vuelve a verificar si está protegido o no. Consulte la salida de la consola para referencia. Antes de la protección, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/) devuelve **false** pero después de la protección, devuelve **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindOutIfVbaProjectIsProtected.go" >}}
## **Salida de la consola**

Esta es la salida en consola del código de muestra anterior como referencia.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
