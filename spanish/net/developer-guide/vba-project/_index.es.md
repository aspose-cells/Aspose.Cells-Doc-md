---
title: Administre los códigos VBA del libro de Excel habilitado para macros.
linktitle: Proyecto macro
type: docs
weight: 200
url: /es/net/manage-vba-project/
description: Agregue el módulo VBA y modifique VBA o macro con la biblioteca Aspose.Cells.
---
## **Agregue un módulo VBA en C#**
{{% alert color="primary" %}}

 Aspose.Cells le permite agregar un nuevo módulo VBA y código de macro usando Aspose.Cells. Utilice el[**Libro de trabajo.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) método para agregar el nuevo Módulo VBA dentro del libro de trabajo

{{% /alert %}}

El siguiente código de ejemplo crea un nuevo libro de trabajo y agrega un nuevo módulo VBA y código de macro y guarda el resultado en formato XLSM. Una vez, abrirá el archivo XLSM de salida en Microsoft Excel y haga clic en el**Desarrollador > Visual Basic** comandos de menú, verá un módulo llamado "TestModule" y dentro de él, verá el siguiente código de macro.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aquí está el código de muestra para generar el archivo XLSM de salida con el módulo VBA y el código de macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Modificar VBA o Macro en C#**

{{% alert color="primary" %}} 

Puede modificar VBA o código de macro usando Aspose.Cells. Aspose.Cells ha agregado el siguiente espacio de nombres y clases para leer y modificar el proyecto de VBA en el archivo de Excel.

- Aspose.Cells.Vba
- Proyecto Vba
- VbaModuleCollection
- Módulo Vba

Este artículo le mostrará cómo cambiar el código VBA o macro dentro del archivo fuente de Excel usando Aspose.Cells.

{{% /alert %}} 

El siguiente código de muestra carga el archivo fuente de Excel que tiene un código VBA o macro siguiente dentro de él.

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Después de la ejecución del código de muestra Aspose.Cells, el código VBA o Macro se modificará de esta manera

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Puedes descargar el[archivo fuente de Excel](5112508.xlsm) y el[archivo de salida de Excel](5112511.xlsm) de los enlaces dados.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Temas avanzados**
- [Agregue una referencia de biblioteca al proyecto VBA en el libro de trabajo](/cells/es/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Asignar macro al control de formulario](/cells/es/net/assign-macro-to-form-control/)
- [Compruebe si la firma digital del código VBA es válida](/cells/es/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Compruebe si el código VBA está firmado](/cells/es/net/check-if-vba-code-is-signed/)
- [Compruebe si el proyecto de VBA en un libro de trabajo está firmado](/cells/es/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Compruebe si el proyecto VBA está protegido y bloqueado para su visualización](/cells/es/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copie VBA Macro UserForm DesignerStorage de la plantilla al libro de trabajo de destino](/cells/es/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firme digitalmente un proyecto de código VBA con certificado](/cells/es/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportar certificado VBA a archivo o transmisión](/cells/es/net/export-vba-certificate-to-file-or-stream/)
- [Filtre el proyecto VBA mientras carga un libro de trabajo](/cells/es/net/filter-vba-project-while-loading-a-workbook/)
- [Averigüe si el proyecto VBA está protegido](/cells/es/net/find-out-if-vba-project-is-protected/)
- [Proteger con contraseña el proyecto VBA del libro de Excel](/cells/es/net/password-protect-the-vba-project-of-excel-workbook/)

