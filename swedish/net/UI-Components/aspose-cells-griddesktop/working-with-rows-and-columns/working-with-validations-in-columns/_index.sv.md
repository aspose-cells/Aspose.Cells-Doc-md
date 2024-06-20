---
title: Arbeta med valideringar i kolumner
type: docs
weight: 80
url: /sv/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop, validering, valideringar
description: Den här artikeln introducerar hur man använder valideringar i kolumner i GridDesktop.
---

{{% alert color="primary" %}} 

I ett av våra tidigare ämnen har vi diskuterat om valideringar, men det var i sammanhanget [Valideringar i Arbetsblad](/cells/sv/net/working-with-validations-in-worksheets/) (för allmän information om validering och valideringslägen, kan utvecklare hänvisa till det här ämnet). I det här ämnet förklarar vi valideringar med avseende på kolumner. Genom den här funktionen är det möjligt för utvecklare att tillämpa en valideringsregel på vilken kolumn som helst i arbetsbladet. Låt oss diskutera det i detalj.

{{% /alert %}} 
## **Lägga till validering i kolumnen**
För att lägga till vilken typ av validering som helst i en kolumn, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- **Lägg till** en önskad **validering** till en valfri kolumn

**VIKTIGT:** För mer information om typer av validering (eller valideringlägen som **Obligatorisk validering**, **Regular Expressions Validering** och **Anpassad validering**) och implementering av **Anpassad validering**, vänligen se [Arbeta med validering i kalkylblad](/cells/sv/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Åtkomst till kolumnvalidering**
För att komma åt en specifik kolumnvalidering, följ stegen nedan:

- Kom åt ett önskat **Kalkylblad**
- Åtkomst till en specifik kolumn **Validering** i **Kalkylbladet**
- Redigera **Validering**-attribut, om önskat



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Ta bort kolumnvalidering**
För att ta bort en specifik kolumnvalidering från kalkylbladet, följ stegen nedan:

- Kom åt ett önskat **Kalkylblad**
- Ta bort en specifik kolumn **Validering** från **Kalkylbladet**



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
