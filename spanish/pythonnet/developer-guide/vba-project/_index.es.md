---
title: Gestiona los códigos VBA de libros de Excel habilitados para macros.
linktitle: Proyecto de Macros
type: docs
weight: 200
url: /es/python-net/manage-vba-project/
description: Agregar módulo VBA y modificar VBA o Macro con la biblioteca Aspose.Cells para Python via .NET.
---

## **Agregar un módulo VBA en Python**
{{% alert color="primary" %}}

Aspose.Cells te permite agregar un nuevo módulo VBA y código Macro usando Aspose.Cells para Python via .NET. Por favor, usa el método [**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/) para agregar el nuevo módulo VBA dentro del libro de trabajo

{{% /alert %}}

El siguiente código de ejemplo crea un nuevo libro de trabajo y agrega un nuevo módulo de VBA y código de macro, y guarda la salida en formato XLSM. Una vez que abras el archivo de salida XLSM en Microsoft Excel y hagas clic en los comandos del menú **Desarrollador > Visual Basic**, verás un módulo llamado "TestModule" y dentro de él verás el siguiente código de macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aquí tienes el código de ejemplo para generar el archivo de salida XLSM con módulo de VBA y código de macro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AddVBAModuleOrCode.py" >}}

## **Modificar VBA o Macro en Python**

{{% alert color="primary" %}} 

Puedes modificar el código VBA o Macro usando Aspose.Cells para Python via .NET. Aspose.Cells para Python via .NET ha añadido los siguientes espacios de nombres y clases para leer y modificar el proyecto VBA en el archivo de Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Este artículo te mostrará cómo cambiar el código VBA o Macro dentro del archivo Excel original usando Aspose.Cells para Python via .NET.

{{% /alert %}} 

El siguiente código de ejemplo carga el archivo de Excel fuente que contiene el siguiente código de VBA o macro.

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Después de la ejecución del código ejemplo de Aspose.Cells para Python via .NET, el código VBA o Macro se modificará así

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Puedes descargar el [archivo de Excel fuente](5112508.xlsm) y el [archivo de Excel de salida](5112511.xlsm) desde los enlaces proporcionados.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-ModifyingVBAOrMacroCode.py" >}}

## **Temas avanzados**
- [Agregar una referencia de librería al proyecto de VBA en el libro de trabajo](/cells/es/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [Comprobar si la firma digital del código VBA es válida](/cells/es/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [Comprobar si el código VBA está firmado](/cells/es/python-net/check-if-vba-code-is-signed/)
- [Comprobar si el proyecto de VBA en un libro de Excel está firmado](/cells/es/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [Comprobar si el proyecto de VBA está protegido y bloqueado para ver](/cells/es/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Firmar digitalmente un proyecto de código VBA con certificado](/cells/es/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportar certificado de VBA a archivo o flujo de datos](/cells/es/python-net/export-vba-certificate-to-file-or-stream/)
- [Filtrar proyecto de VBA al cargar un libro de Excel](/cells/es/python-net/filter-vba-project-while-loading-a-workbook/)
- [Descubrir si el proyecto de VBA está protegido](/cells/es/python-net/find-out-if-vba-project-is-protected/)
- [Proteger con contraseña el proyecto de VBA del libro de Excel](/cells/es/python-net/password-protect-the-vba-project-of-excel-workbook/)

