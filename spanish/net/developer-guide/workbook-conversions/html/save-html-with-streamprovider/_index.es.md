---
title: Guardar HTML con StreamProvider
type: docs
weight: 80
url: /es/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

Al convertir archivos de Excel que contienen imágenes y formas en archivos HTML, a menudo nos enfrentamos a los siguientes dos problemas:
1. ¿Dónde debemos guardar las imágenes y formas al guardar el archivo de Excel en un stream HTML?
1. Reemplazar la ruta predeterminada con la ruta esperada.

Este artículo explica cómo implementar la interfaz [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) para establecer la propiedad [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider). Al implementar esta interfaz, podrá guardar los recursos creados durante la generación de HTML en ubicaciones específicas o en streams de memoria.

{{% /alert %}} 

Este es el código principal que muestra el uso de la propiedad [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Aquí está el código para la clase *ExportStreamProvider*, que implementa la interfaz [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) utilizada dentro del código anterior.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

