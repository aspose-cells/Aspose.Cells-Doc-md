---
title: Agregue una referencia de biblioteca al proyecto VBA en el libro de trabajo
type: docs
weight: 10
url: /es/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

 En Microsoft Excel, puede agregar una referencia de biblioteca al proyecto de VBA haciendo clic en el**Herramientas > Referencias...** a mano. Se abrirá el siguiente cuadro de diálogo que le ayudará a seleccionar entre las referencias existentes o explorar su biblioteca usted mismo.

![todo:imagen_alternativa_texto](add-a-library-reference-to-vba-project-in-workbook_1.png)

 Pero a veces, debe agregar o registrar la referencia de la biblioteca al proyecto de VBA a través del código. Puedes hacerlo usando el Aspose.Cells[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) método.

{{% /alert %}}

## **Agregue una referencia de biblioteca al proyecto VBA en el libro de trabajo**

 El siguiente código de muestra agrega o registra dos referencias de biblioteca al proyecto de VBA del libro de trabajo usando[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
