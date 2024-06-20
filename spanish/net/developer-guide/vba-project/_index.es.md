---
title: Gestiona los códigos VBA de libros de Excel habilitados para macros.
linktitle: Proyecto de Macros
type: docs
weight: 200
url: /es/net/manage-vba-project/
description: Agregar un módulo de VBA y modificar el VBA o Macro con la librería Aspose.Cells.
---

## **Agregar un módulo de VBA en C#**
{{% alert color="primary" %}}

Aspose.Cells te permite agregar un nuevo módulo de VBA y código de macro utilizando Aspose.Cells. Por favor, utiliza el método [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) para agregar el nuevo módulo de VBA dentro del libro de trabajo

{{% /alert %}}

El siguiente código de ejemplo crea un nuevo libro de trabajo y agrega un nuevo módulo de VBA y código de macro, y guarda la salida en formato XLSM. Una vez que abras el archivo de salida XLSM en Microsoft Excel y hagas clic en los comandos del menú **Desarrollador > Visual Basic**, verás un módulo llamado "TestModule" y dentro de él verás el siguiente código de macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aquí tienes el código de ejemplo para generar el archivo de salida XLSM con módulo de VBA y código de macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Modificar el VBA o Macro en C#**

{{% alert color="primary" %}} 

Puedes modificar el código de VBA o macro utilizando Aspose.Cells. Aspose.Cells ha añadido el siguiente espacio de nombres y clases para leer y modificar el proyecto de VBA en el archivo de Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Este artículo te mostrará cómo cambiar el código de VBA o macro dentro del archivo de Excel fuente utilizando Aspose.Cells.

{{% /alert %}} 

El siguiente código de ejemplo carga el archivo de Excel fuente que contiene el siguiente código de VBA o macro.

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Después de la ejecución del código de ejemplo de Aspose.Cells, el código de VBA o macro será modificado de la siguiente manera

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Puedes descargar el [archivo de Excel fuente](5112508.xlsm) y el [archivo de Excel de salida](5112511.xlsm) desde los enlaces proporcionados.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Temas avanzados**
- [Agregar una referencia de librería al proyecto de VBA en el libro de trabajo](/cells/es/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Asignar Macro a un control de formulario](/cells/es/net/assign-macro-to-form-control/)
- [Comprobar si la firma digital del código VBA es válida](/cells/es/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Comprobar si el código VBA está firmado](/cells/es/net/check-if-vba-code-is-signed/)
- [Comprobar si el proyecto de VBA en un libro de Excel está firmado](/cells/es/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Comprobar si el proyecto de VBA está protegido y bloqueado para ver](/cells/es/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino](/cells/es/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firmar digitalmente un proyecto de código VBA con certificado](/cells/es/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportar certificado de VBA a archivo o flujo de datos](/cells/es/net/export-vba-certificate-to-file-or-stream/)
- [Filtrar proyecto de VBA al cargar un libro de Excel](/cells/es/net/filter-vba-project-while-loading-a-workbook/)
- [Descubrir si el proyecto de VBA está protegido](/cells/es/net/find-out-if-vba-project-is-protected/)
- [Proteger con contraseña el proyecto de VBA del libro de Excel](/cells/es/net/password-protect-the-vba-project-of-excel-workbook/)

