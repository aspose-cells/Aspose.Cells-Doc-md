---
title: Trabajar con Validaciones en Columnas
type: docs
weight: 80
url: /es/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

 En uno de nuestros temas anteriores, hemos discutido acerca de las validaciones, pero eso fue en el contexto de[Validaciones en hojas de trabajo](/cells/es/net/working-with-validations-in-worksheets/) (para tener información general sobre la validación y los modos de validación, los desarrolladores pueden consultar este tema). En este tema, explicaremos las validaciones con respecto a las columnas. Con esta función, los desarrolladores pueden aplicar una regla de validación en cualquier columna de la hoja de trabajo. Vamos a discutirlo en detalle.

{{% /alert %}} 
## **Agregar validación de columna**
Para agregar cualquier tipo de validación a una columna, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
- **Agregar** un deseado**Validación** a cualquier columna

**IMPORTANTE:**Para obtener más información sobre los tipos de validación (o modos de validación como**Se Requiere Validación**, **Validación de expresiones regulares** y**Validación personalizada** ) e implementar**Validación personalizada** , por favor refiérase a[Trabajando con Validaciones en Hojas de Trabajo.](/cells/es/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Acceso a la validación de columnas**
Para acceder a una validación de columna específica, siga los pasos a continuación:

-  Accede a un deseado**Hoja de cálculo**
-  Acceder a una columna específica**Validación** en el**Hoja de cálculo**
-  Editar**Validación** atributos, si se desea



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Eliminación de la validación de columnas**
Para eliminar una validación de columna específica de la hoja de trabajo, siga los pasos a continuación:

-  Accede a un deseado**Hoja de cálculo**
-  Eliminar una columna específica**Validación** desde el**Hoja de cálculo**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
