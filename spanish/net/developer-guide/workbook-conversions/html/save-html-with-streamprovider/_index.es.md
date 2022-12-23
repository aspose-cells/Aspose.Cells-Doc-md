---
title: Guardar HTML con StreamProvider
type: docs
weight: 80
url: /es/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

Al convertir campos de Excel que contienen imágenes y formas en archivos html, a menudo nos enfrentamos a los siguientes dos problemas:
1. ¿Dónde debemos guardar las imágenes y las formas al guardar el archivo de Excel en la transmisión html?
1. Reemplace la ruta predeterminada con la ruta exceptuada.

 Este artículo explica cómo implementar[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interfaz para configurar el[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) propiedad. Al implementar esta interfaz, podrá guardar los recursos creados durante la generación HTML en sus ubicaciones o flujos de memoria específicos.

{{% /alert %}} 

 Este es el código principal que muestra el uso de[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)propiedad



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



 Aquí está el código para*ExportStreamProviderExportStreamProvider* clase que implementa[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)interfaz utilizada dentro del código anterior.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

