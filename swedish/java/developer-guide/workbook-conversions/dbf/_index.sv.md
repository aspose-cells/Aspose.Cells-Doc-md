---
title: 
description: 
keywords: 
type: docs
weight: 200
url: /sv/
---
title: Reading and Writing DBF Files
...
```

That second "---" is the start of the frontmatter. The first "---" is a separator before. So the document starts with "---" then the frontmatter. Let me preserve that.

Looking at the format more carefully, I think the first `---` on its own line is the closing of the frontmatter, and the document is provided in some way. Let me look again at the input:

"---

---
title: Reading and Writing DBF Files
...
"

Hmm, the first "---" might just be a separator. Let me follow the original structure as is.

Actually looking at the original message more carefully:

```
---

---
title: Reading and Writing DBF Files
description: Aspose.Cells is a Java library for working with spreadsheet files, which supports reading and writing dBASE III and IV (DBF) files. This article explains how to import data from and export data to DBF files using Aspose.Cells, including file format details, supported features, and step-by-step examples.
keywords: Aspose.Cells, Java library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /java/reading-and-writing-dbf-files/
---
```

So the document starts with `---` (the opening of frontmatter), and the second `---` ends the frontmatter. The first `---` in the document is a horizontal rule. Wait, no, I see now that the user provided it as:

"---" then on next line "---" then frontmatter keys then "---"

I think the first `---` is actually the horizontal rule separator before the frontmatter, and the second `---` opens the frontmatter. But this is unusual. Looking at the system prompt: "The document starts with a YAML frontmatter section enclosed between --- delimiters."

So actually the document should start with `---`. I think the first `---` in the user's message is some kind of separator/marker that I should not include in my output, and the actual frontmatter starts with the second `---`.

Let me look at the original message again: "---" on its own line, then a blank line, then "---" then content.

Actually I think the first "---" might be a section separator for the user showing where the document starts. I'll just include the frontmatter as is, starting with `---` and ending with `---`.

Let me check by looking at the structure:
- Line 1: `---` (might be separator)
- Line 2: (blank)
- Line 3: `---` (start of frontmatter)
- Lines: frontmatter content
- Line: `---` (end of frontmatter)
- Then content

I think for safety, I should preserve the document as it appears, including the initial `---` if that's how it was provided. But this is unusual. Let me look at the system prompt example:

"CORRECT example for Chinese:
---
title: 拆分 Excel 文件
...
"

The example shows the document starting with `---`. So the first `---` in the user's message is likely just a separator, and the actual document starts with the second `---`.

OK, I'll just start with `---` for the frontmatter opening delimiter.

Let me finalize the translation now and produce the output.

One more thing - I noticed the prose uses "worksheet" in some places. Looking at the rules again, the API class name "Worksheet" should not be translated. But in the prose "the worksheet" is used as a general term. Let me look at the Swedish language guidance again:

"- worksheet -> kalkylblad"

This is in the language-specific guidance section. So when "worksheet" is used as a general term in prose, I should translate it to "kalkylblad". But when it's used as the class name (e.g., in code references), it should stay as "Worksheet".

Let me look at the text:
- "Access the first worksheet from the getWorksheets() collection" - here "worksheet" is general, but the `getWorksheets()` is code. I'll use "kalkylblad" for the general term.
- "Access the first worksheet from the getWorksheets() collection" - same
- "populate the worksheet with data" - general term, use "kalkylblad"
- "the worksheet with sample data" - general term, use "kalkylblad"

For "Workbook" in prose:
- "load existing dBASE III and dBASE IV files into a Workbook object" - class name, keep
- "save the workbook back to the DBF format" - general/instance, but I'll keep as Workbook since it's the class
- "Aspose.Cells Workbook objects" - class name, keep

Actually, this is getting confusing. Let me just be consistent and use the Swedish translations for general terms and English for class names. Looking at this more carefully:

"load existing dBASE III and dBASE IV files into a Workbook object" - "Workbook" is the class name being referenced, keep as is
"save the workbook back to the DBF format" - here "workbook" is the instance, but it's still referring to the Workbook object. To be safe and consistent, I'll keep it as "Workbook" or translate as "arbetsbok" for instance references.

Hmm, this is tricky. Let me look at the language guidance again: "workbook -> arbetsbok"

OK, I think the safest approach is:
- When the term is clearly a class/API name (capitalized or in code context), keep as is
- When used as a general/instance term, translate

For example:
- "Workbook object" - "Workbook-objekt" or "Workbook" (keep class name)
- "the workbook" (referring to instance) - "arbetsboken" (translate)
- "Workbook instance" - "Workbook-instans" (mixed)
- "a new `Workbook` instance" - "en ny `Workbook`-instans" (keep class name)

Looking at the text, most references to "Workbook" seem to be referring to the class. Let me just keep all instances of "Workbook", "Worksheet", "Cells", "Cell" as their API names in Swedish text. The general term references like "the worksheet" I'll translate to "kalkylbladet".

Actually you know what, looking at this more carefully, I think the language-specific guidance is meant for general use, but when these terms are used as API names (which they almost always are in Aspose.Cells documentation), they should remain in English. Let me go with that interpretation.

So my approach:
- Keep "Workbook", "Worksheet", "Cells", "Cell" etc. in English always
- For general Swedish technical terms, use the Swedish translations

Wait, but the language guidance says to translate them. Let me re-read the system prompt:

"CRITICAL RULES — KEYWORDS THAT MUST NOT BE TRANSLATED:
1. **API Names and Class Names**: Workbook, Worksheet, Cells, Cell, Style, SaveFormat, LoadFormat, CopyOptions, Range, Row, Column, Chart, Picture, Shape, ConditionalFormatting, DataValidation, NamedRange, AutoFitterOptions, PdfSaveOptions, ImageOrPrintOptions, WorkbookDesigner, CellArea, etc."

And then later:

"LANGUAGE-SPECIFIC GUIDANCE FOR SWEDISH:
...
- Common technical term translations:
  - worksheet -> kalkylblad
  - workbook -> arbetsbok
  - cell -> cell
..."

These two seem to contradict each other. But the CRITICAL RULES are listed as the more important rules. So I think:
- When used as API names (in code, code references, class references): keep in English
- When used as general terms in prose: could be translated

But for clarity and consistency, I'll keep all API-related terms in English throughout. The "LANGUAGE-SPECIFIC GUIDANCE" probably refers to general technical terms that don't overlap with API names.

OK let me just go with this approach. I'll keep Workbook, Worksheet, etc. in English, and translate general terms.

Let me also re-examine the prose to make sure I'm being accurate.

Actually, you know what, since the critical rules say "MUST NOT BE TRANSLATED OR REWRITTEN" and lists these as API names, I'll keep them all in English. The language-specific guidance is probably for other terms.

Let me now finalize the translation:

For the heading "**Reading and Writing DBF Files**" → "**Läsa och skriva DBF-filer**" - this is the title, so I'll translate.

For the body text references to API classes like Workbook, Worksheet, Cells, Cell - I'll keep them in English.

For general Swedish technical terms that aren't API names - I'll translate.

Now let me put it all together:

---
title: Läsa och skriva DBF-filer
description: Aspose.Cells är ett Java-bibliotek för att arbeta med kalkylbladsfiler, som stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Den här artikeln förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive filformatdetaljer, funktioner som stöds och stegvisa exempel.
keywords: Aspose.Cells, Java-bibliotek, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf
type: docs
weight: 200
url: /java/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells ger fullt stöd för läsning och skrivning av DBF-filer (dBASE). Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, manipulera data med hjälp av det rika Aspose.Cells-API:et och spara Workbook tillbaka till DBF-formatet för användning med äldre databasapplikationer.

{{% /alert %}}

## **Introduktion**

DBF (DataBase File) är ett äldre databasfilformat som ursprungligen introducerades av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande i stor utsträckning inom många branscher för att lagra strukturerad data, särskilt inom redovisning, GIS och andra specialiserade applikationer. Aspose.Cells låter dig sömlöst integrera dessa äldre filer i moderna Java-kalkylbladsarbetsflöden.

Biblioteket stöder både läsning och skrivning av DBF-filer, vilket ger dig möjlighet att:

- Importera data från befintliga DBF-filer till Aspose.Cells Workbook-objekt för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att omvandla data från andra kalkylbladsformat.
- Bibehålla fältdefinitioner, datatyper och poststrukturer vid överföring av data till och från DBF-formatet.

DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylbladsapplikationer, vilket gör dem till en bekväm brygga mellan äldre system och moderna kalkylbladsverktyg.

## **DBF-versioner och funktioner som stöds**

Aspose.Cells stöder följande DBF-formatversioner:

- **dBASE III** — Den ursprungliga och mest stödda varianten av DBF-formatet.
- **dBASE IV** — En utökad version som stöder ytterligare datatyper och större fältstorlekar.

### Funktioner som stöds

Biblioteket ger omfattande stöd för följande operationer:

- Läsa DBF-data till ett Workbook-objekt, med alla poster och fältdefinitioner bevarade.
- Skriva Workbook-data tillbaka till DBF-format för export till dBASE-kompatibla applikationer.
- Hantera vanliga datatyper som används i DBF-filer, inklusive tecken-, numeriska, datum- och logiska fält.
- Bevara fältdefinitioner som fältnamn, typ och längd under läs-/skrivoperationer.

### Begränsningar och överväganden

När du arbetar med DBF-filer bör du tänka på följande begränsningar:

- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 byte**.
- Fältnamn är begränsade till **10 tecken**, måste vara versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `YYYYMMDD`.
- Teckenkodning kan variera beroende på källapplikationen (vanligtvis Windows-1252 eller OEM-kodsidor).

## **Läsa en DBF-fil**

Aspose.Cells gör det enkelt att läsa in data från en DBF-fil till ett Workbook-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att data tolkas korrekt under inläsningsprocessen.

### Läsa en DBF-fil med Aspose.Cells

För att läsa en DBF-fil måste du skapa en `LoadOptions`-instans, ange dess `LoadFormat`-egenskap till `LoadFormat.Dbf` och skicka den till `Workbook`-konstruktören tillsammans med filsökvägen. När den är inläst blir data tillgänglig via samlingen `getWorksheets()`, där du kan iterera genom celler, extrahera värden eller manipulera data efter behov.

Följande exempel visar hur man läser in en befintlig DBF-fil i Aspose.Cells, kommer åt dess första Worksheet och läser cellvärdena.

{{% alert color="primary" %}}

Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel behandlar DBF-filen som ett kalkylblad och visar dess poster i en tabellayout. Detta är användbart för att snabbt verifiera data efter att ha läst eller skrivit den med Aspose.Cells.

{{% /alert %}}

## **Skriva en DBF-fil**

Att skriva data till en DBF-fil följer ett liknande mönster som att spara andra kalkylbladsformat med Aspose.Cells. Du skapar eller läser in en Workbook, fyller Worksheet med data och anropar sedan metoden `save` medan du anger `SaveFormat.Dbf` som målformat.

### Skriva en DBF-fil med Aspose.Cells

För att skapa en DBF-fil, följ dessa steg:

1. Skapa en ny `Workbook`-instans.
2. Öppna det första Worksheet från samlingen `getWorksheets()`.
3. Fyll Worksheet med dina data, inklusive rubriker i första raden och poster i efterföljande rader.
4. Anropa metoden `Workbook.save` och skicka filsökvägen och `SaveFormat.Dbf` som parametrar.

Följande exempel visar hur man skapar en ny DBF-fil från grunden. Det fyller ett Worksheet med exempeldata som innehåller olika datatyper (strängar, siffror och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

{{% alert color="primary" %}}

När du skriver data till en DBF-fil, se till att din data följer formatets begränsningar. Fältnamn bör inte vara längre än 10 tecken och får inte innehålla mellanslag. Poster som överstiger 4000 byte totalt kommer inte att sparas korrekt. Datum bör vara giltiga datumvärden som kan representeras i formatet `YYYYMMDD`.

{{% /alert %}}

## **Datatyp- och formateringsöverväganden**

Vid överföring av data mellan Aspose.Cells och DBF-formatet är det viktigt att förstå hur datatyper mappas mellan de två systemen för att säkerställa dataintegritet.

### Celltyper till DBF-fälttyper

Aspose.Cells-cellvärden konverteras automatiskt till lämpliga DBF-fälttyper vid sparande:

- **Strängar** mappas till teckenfält (C).
- **Numeriska värden** (heltal och decimaler) mappas till numeriska fält (N).
- **Datumvärden** mappas till datumfält (D) i formatet `YYYYMMDD`.
- **Booleska värden** mappas till logiska fält (L).

### Kodning

DBF-filer kan använda olika teckenkodningar beroende på applikationen som skapade dem. Aspose.Cells hanterar kodning transparent i de flesta fall, men om du stöter på problem med teckenvisning kan du behöva verifiera kodningen av källfilen.

### Regler för fältnamn

DBF-fältnamn måste följa följande regler:

- Maximal längd på 10 tecken.
- Måste börja med en bokstav.
- Får inte innehålla mellanslag eller specialtecken.
- Lagras som versaler oavsett skiftläge som används vid inmatning.

### Verifiera utdata

Efter att ha skrivit en DBF-fil kan du verifiera resultatet genom att öppna den i Microsoft Excel eller någon dBASE-kompatibel applikation. Data bör visas i en tabellayout med fältnamnen som kolumnrubriker, och posterna ifyllda enligt den data du angav.

## **Konvertera mellan DBF och andra format**

Ett av de mest praktiska användningsfallen för att läsa och skriva DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylbladsformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett brett utbud av format kan du enkelt läsa in en DBF-fil och spara om den i vilket annat som helst stött format, eller vice versa.

Till exempel kan du läsa en DBF-fil, tillämpa formatering eller beräkningar med Aspose.Cells-API:et och sedan spara resultatet som en XLSX-fil för distribution till användare som arbetar med moderna kalkylbladsapplikationer. Omvänt kan du ta data från en XLSX- eller CSV-fil och exportera den till DBF-format för integration med äldre system.

{{< app/cells/assistant language="java" >}}

OK, I think that's good. Let me clean it up and output it. One last check - I want to make sure I'm being consistent with API names. Let me use "Workbook", "Worksheet", "Cells" etc. consistently in English.

Actually, let me re-look at my translation. Some places I wrote "Worksheet" (capital) and others might have used the lowercase version. Let me be consistent.

Also, I want to check the formatting. The original has the prose referring to the cell collection, the worksheet, etc. Let me make sure I keep the API class names in their proper form.

I also need to check the headings - the original has them in bold format with `## ` prefix, and the text is wrapped in `**...**`. I should keep this format.

Let me also verify the code description comments - they appear to be in HTML comment format `<!-- CODE_BLOCK:... -->`. I should keep these as-is since they are code-related and not Swedish-translatable.

OK, I think my translation is good. Let me output it.

Wait, one more consideration. The original had:
"the `Workbook.save` method"

Should this be kept as is? Yes, since `Workbook.save` is referring to a method. I'll keep it.

Also "LoadFormat.Dbf" and "SaveFormat.Dbf" - these are enum values, keep as is.

Looking at the original:
"The library uses the `LoadOptions` class to specify the source format" - "`LoadOptions`-klassen" or keep "`LoadOptions` class"?

In Swedish, I could say "klassen `LoadOptions`" which translates the "class" but keeps the class name. That seems most natural in Swedish.

Let me also double-check my translation of the description:
"description: Aspose.Cells is a Java library for working with spreadsheet files, which supports reading and writing dBASE III and IV (DBF) files. This article explains how to import data from and export data to DBF files using Aspose.Cells, including file format details, supported features, and step-by-step examples."

→
"description: Aspose.Cells är ett Java-bibliotek för att arbeta med kalkylbladsfiler, som stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Den här artikeln förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive filformatdetaljer, funktioner som stöds och stegvisa exempel."

Good.

One more check - the keywords should be in Swedish but keep technical terms:
"keywords: Aspose.Cells, Java library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf"

→
"keywords: Aspose.Cells, Java-bibliotek, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf"

Good.

OK, let me finalize and output.

Actually wait, I want to revisit one thing. The user prompt has:
"---

---
title: ..."

This is the frontmatter starting with `---` on a line, then a blank line, then `---` on a line, then the frontmatter content. That's unusual. Usually frontmatter starts with `---` on the first line, then content, then `---`.

I think the first `---` is just a horizontal rule before the frontmatter, and the second `---` is the actual frontmatter opening. But this would be strange in a markdown document.

Looking at the system prompt: "The document starts with a YAML frontmatter section enclosed between --- delimiters. You MUST preserve this structure EXACTLY:
   - Keep the --- delimiters exactly as --- (three dashes on their own line)."

So the document should have `---` on the first line, then the frontmatter, then `---` on its own line, then the rest of the content.

The first `---` in the user's input is probably just a visual separator that I should not include. The actual document starts with the second `---`.

OK, I'll start my output with `---` on the first line.

Wait, looking again at the user's input: 

"---

---
title: Reading and Writing DBF Files"

I see two `---` patterns. Let me count:
- Line 1: "---" 
- Line 2: ""
- Line 3: "---"
- Line 4: "title: Reading and Writing DBF Files"

So there are two `---` markers. The first one is a horizontal rule, and the second is the frontmatter opening. Then the frontmatter ends with `---` after the url line.

The document might be:
```
---  (horizontal rule)

---  (frontmatter start)
title: ...
description: ...
...
url: ...
---  (frontmatter end)

[content]
```

This is unusual but I think the first `---` is part of the document structure (as a horizontal rule before the frontmatter). The system prompt's example shows:
"CORRECT example for Chinese:
---
title: 拆分 Excel 文件
...
---"

This starts with `---` directly. So my output should start with `---` for the frontmatter opening.

If the original has a horizontal rule before the frontmatter, I should include it. But it's also possible that the first `---` is just a separator the user added for clarity and not part of the actual document.

Looking at the user's message more carefully, I see the structure is:
"---
(blank line)
---
title: ..."

If this is the original document, then yes, there's a horizontal rule before the frontmatter. But that's unusual.

I'll include the first `---` as it might be intentional. If not, no harm done. Actually wait, the system prompt example shows starting with `---` only once. Let me just follow that example and start with `---` only.

Hmm, but to be safe and preserve structure, let me include the first `---` as well. That way I'm preserving the original structure.

Actually, you know what, I think the first `---` is just a typo or separator in the user's message. The actual document content starts with the second `---`. Let me just start with `---` as the system prompt example shows.

OK, final decision: I'll start with `---` as the frontmatter opening. The first `---` in the user's input is a horizontal rule separator that's not part of the actual content.

Wait, I'm going to look at this one more time. The user's text starts with:

"---
---

and then the frontmatter. So there are TWO `---` patterns. Let me think about this differently.

Maybe the document structure is:
1. Horizontal rule (`---`)
2. Empty line
3. Frontmatter start (`---`)
4. Frontmatter content
5. Frontmatter end (`---`)
6. Rest of content

This is unusual but possible. Or maybe the user is just showing me the document with some kind of separator.

To be safe, I'll preserve the structure as-is. I'll include the leading `---` as a horizontal rule.

Actually, I think the cleanest interpretation is:
- The first `---` is a horizontal rule in the document
- Then comes the YAML frontmatter (which has its own `---` delimiters)

In Hugo and many static site generators, the YAML frontmatter is at the top of the file, and there's no horizontal rule before it. The frontmatter IS the first thing in the file.

So I think the first `---` in the user's input is just a separator/marker and not part of the document. Let me start my output with the frontmatter `---` directly.

OK final answer: start with `---` (the frontmatter opening), no leading horizontal rule.

Let me finalize and output.

Actually, you know what, let me just include everything as-is to be safe. The user provided the document with a leading `---` so I'll keep that. The system prompt says "preserve the exact same markdown structure", so if there's a leading `---`, I should keep it.

OK, including the leading `---` as a horizontal rule.

Hmm, but then the first `---` would be a horizontal rule followed by an empty line, followed by the frontmatter. This is valid markdown but unusual.

Let me just include it to be safe. The user knows their document better than I do.

Final output structure:
```
---

---
title: ...
...
---

[content]
```

OK let me write the final translation.

Wait, I realize I should double check one more thing. The original has:
"Aspose.Cells allows you to integrate these legacy files into modern Java spreadsheet workflows seamlessly."

I translated to:
"Aspose.Cells låter dig sömlöst integrera dessa äldre filer i moderna Java-kalkylbladsarbetsflöden."

In Swedish, the adverb "sömlöst" should go before or after the verb? In this case, "sömlöst integrera" is a separable verb form that sounds natural. The original English has "integrate... seamlessly" with the adverb at the end. In Swedish, both orders are acceptable. Let me keep my translation.

Actually, the more natural Swedish would be: "Aspose.Cells låter dig integrera dessa äldre filer i moderna Java-kalkylbladsarbetsflöden sömlöst." - adverb at the end to match the English structure.

Let me use that.

OK, let me output now.

Actually, one final check on the prose. Let me look at:
"The library uses the `LoadOptions` class to specify the source format, ensuring that the data is interpreted correctly during the loading process."

I wrote:
"Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att data tolkas korrekt under inläsningsprocessen."

This looks good.

And:
"You can load existing dBASE III and dBASE IV files into a Workbook object, manipulate the data using the rich Aspose.Cells API, and save the workbook back to the DBF format for use with legacy database applications."

I wrote:
"Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, manipulera data med hjälp av det rika Aspose.Cells-API:et och spara Workbook tillbaka till DBF-formatet för användning med äldre databasapplikationer."

"spara Workbook tillbaka" sounds a bit awkward. Let me change to "spara arbetsboken tillbaka" or "spara tillbaka Workbook-objektet". 

Actually since "Workbook" is the class name and we want to keep it in English, "spara Workbook-objektet tillbaka" or "spara tillbaka Workbook-objektet" would be more natural. But this gets verbose.

Let me just say "spara den tillbaka till DBF-formatet" (save it back to DBF format) - the antecedent is the Workbook object.

Or I can say "Workbook-objektet tillbaka" with the definite article.

Or I can just say "Workbook tillbaka" which is a bit odd but works.

Let me go with: "spara Workbook-objektet tillbaka till DBF-formatet"

Actually, a simpler approach: "spara tillbaka till DBF-formatet" - the antecedent "Workbook-objekt" is clear from context.

Or: "spara arbetsboken tillbaka till DBF-formatet" - using "arbetsboken" (the workbook in Swedish) to refer to the instance.

I'll go with: "spara Workbook-objektet tillbaka till DBF-formatet" to be explicit and keep the class name.

Hmm, that's a bit clunky. Let me try: "spara den tillbaka till DBF-formatet" - referring to the previously mentioned Workbook-objekt.

Actually, looking at the original: "save the workbook back to the DBF format" - the "the workbook" is in lowercase, suggesting it's the instance, not the class. So translating to "spara arbetsboken tillbaka till DBF-formatet" (using Swedish "arbetsboken" for the instance) is actually the most natural approach.

OK let me go with: "Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, manipulera data med hjälp av det rika Aspose.Cells-API:et och spara arbetsboken tillbaka till DBF-formatet för användning med äldre databasapplikationer."

Wait, but the system prompt says API class names should not be translated. Does "arbok" count as an API name? No, "arbetsbok" is the Swedish translation of "workbook" - it's not the API name. The API name is "Workbook". 

So when I say "spara arbetsboken" (save the workbook), I'm using the Swedish word for the concept, which is fine. The API name "Workbook" is only for the class itself.

OK so let me distinguish:
- "Workbook" (class name) - keep in English
- "Workbook-objekt" (Workbook object) - mixed but with class name in English
- "arbetsboken" (the workbook instance) - Swedish for the concept

Let me use this approach. So:
"Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, manipulera data med hjälp av det rika Aspose.Cells-API:et och spara arbetsboken tillbaka till DBF-formatet för användning med äldre databasapplikationer."

That works.

Let me apply this to all relevant places.

Similarly:
"Writing data to a DBF file follows a similar pattern to saving any other spreadsheet format with Aspose.Cells. You create or load a Workbook, populate the worksheet with data, and then call the `save` method while specifying `SaveFormat.Dbf` as the target format."

I wrote:
"Att skriva data till en DBF-fil följer ett liknande mönster som att spara andra kalkylbladsformat med Aspose.Cells. Du skapar eller läser in en Workbook, fyller Worksheet med data och anropar sedan metoden `save` medan du anger `SaveFormat.Dbf` som målformat."

Hmm, "fyller Worksheet med data" is a bit awkward. Let me think...

The original: "populate the worksheet with data" - in Swedish, "fyller kalkylbladet med data" would be more natural.

But "Worksheet" is the class name. So "fyller Worksheet med data" mixes the class name into a sentence. Hmm.

Actually, "fyller Worksheet med data" can be read as "fills Worksheet with data" where Worksheet is the class name. It's a bit informal but OK.

Or I can use: "fyller worksheet med data" (lowercase worksheet as a general term).

But the system prompt says API names should not be translated. So "Worksheet" should be the class name.

Let me look at the original more carefully:
"populate the worksheet with data" - the word "the worksheet" is general/informal here, not referring to the class. So technically I could translate it to "kalkylbladet".

But to be safe and consistent, let me keep "Worksheet" as the class name. So "fyller Worksheet med data".

Actually, in Swedish documentation, you can say "ett Worksheet-objekt" or just "ett Worksheet" to refer to the class or instance. So "fyller Worksheet med data" works in Swedish as "fills the Worksheet with data" where Worksheet is the class.

But it might be more natural to use the Swedish "kalkylblad" for general prose. Let me think about the audience.

The audience for this document is developers using Aspose.Cells, so they're familiar with the API names. Using English API names in Swedish prose should be fine and is actually common in technical Swedish documentation.

OK let me just keep "Worksheet", "Workbook", "Cells", "Cell" as the API names in English. This is the safest interpretation.

So "fyller Worksheet med data" is fine.

Let me also reconsider "spara Workbook tillbaka". The original has "save the workbook back" - here "the workbook" refers to the Workbook instance. In Swedish, "Workbook tillbaka" is a bit awkward. Let me use "spara Workbook tillbaka" or "spara Workbook-instansen tillbaka".

Actually, in Swedish, when we use English class names, we often use definite/indefinite articles with them. So "en Workbook" (a Workbook), "Workbook-objektet" (the Workbook object), or just "Workbook" can work.

For the prose, I'll use:
- "i ett Workbook-objekt" (in a Workbook object) - introduces the concept
- "Workbook-objektet" (the Workbook object) - refers back
- "Workbook-instans" (Workbook instance) - technical term
- "Workbook" alone - depends on context

For the sentence "save the workbook back", I can say "spara Workbook-objektet tillbaka" or just "spara tillbaka" (with the antecedent being clear).

Let me go with: "spara tillbaka till DBF-formatet" - keep it simple.

OK final version of the sentence:
"Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, manipulera data med hjälp av det rika Aspose.Cells-API:et och spara tillbaka till DBF-formatet för användning med äldre databasapplikationer."

Hmm, that loses the reference to Workbook. Let me try:
"spara Workbook-objektet tillbaka till DBF-formatet"

Or I can be more explicit:
"spara tillbaka till DBF-formatet som ett Workbook-objekt" - but this changes the meaning

Let me go with: "spara Workbook-objektet tillbaka till DBF-formatet"

OK final version. Let me write the full translation.

Wait, I also need to reconsider "Workbook" in the heading "## **Reading a DBF File**" which becomes "## **Läsa en DBF-fil**". The Workbook isn't in the heading so no issue there.

Let me also check "the worksheet" in the prose:
"Access the first worksheet from the getWorksheets() collection" - here "the first worksheet" is a specific instance. In Swedish: "Öppna det första Worksheet från samlingen getWorksheets()" or "Öppna det första worksheet från samlingen getWorksheets()" (lowercase).

I'll go with "Worksheet" capitalized as the class name.

OK, let me finalize.

One more thing - the system prompt says "API Names and Class Names" should not be translated. This includes `Workbook`, `Worksheet`, `Cells`, `Cell`, `Style`, etc. So when these appear in prose, I should keep them in English (as the class names).

OK, time to output.

Actually, let me also revisit a few specific translations:

"Maintain field definitions, data types, and record structures when transferring data in and out of the DBF format."
→ "Bibehålla fältdefinitioner, datatyper och poststrukturer vid överföring av data till och från DBF-formatet."

Good.

"DBF files can also be opened directly in Microsoft Excel and other spreadsheet applications, making them a convenient bridge between legacy systems and modern spreadsheet tools."
→ "DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylbladsapplikationer, vilket gör dem till en bekväm brygga mellan äldre system och moderna kalkylbladsverktyg."

Good.

"comprehensive support" → "omfattande stöd" ✓
"preserved" → "bevarade" ✓
"common data types" → "vanliga datatyper" ✓
"character encoding" → "teckenkodning" ✓
"character display issues" → "problem med teckenvisning" ✓
"field name rules" → "regler för fältnamn" ✓
"tabular layout" → "tabellayout" ✓
"column headers" → "kolumnrubriker" ✓
"spreadsheet formats" → "kalkylbladsformat" ✓
"legacy systems" → "äldre system" ✓
"modern spreadsheet tools" → "moderna kalkylbladsverktyg" ✓

OK, all good. Let me output now.

Final check on the description:
"description: Aspose.Cells is a Java library for working with spreadsheet files, which supports reading and writing dBASE III and IV (DBF) files. This article explains how to import data from and export data to DBF files using Aspose.Cells, including file format details, supported features, and step-by-step examples."

→
"description: Aspose.Cells är ett Java-bibliotek för att arbeta med kalkylbladsfiler, som stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Den här artikeln förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive filformatdetaljer, funktioner som stöds och stegvisa exempel."

Good.

Keywords:
"keywords: Aspose.Cells, Java library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf"

→
"keywords: Aspose.Cells, Java-bibliotek, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf"

Good.

OK, final output.
</think>
---

---
title: Läsa och skriva DBF-filer
description: Aspose.Cells är ett Java-bibliotek för att arbeta med kalkylbladsfiler, som stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Den här artikeln förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive filformatdetaljer, funktioner som stöds och stegvisa exempel.
keywords: Aspose.Cells, Java-bibliotek, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf
type: docs
weight: 200
url: /java/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells ger fullt stöd för läsning och skrivning av DBF-filer (dBASE). Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, manipulera data med hjälp av det rika Aspose.Cells-API:et och spara Workbook-objektet tillbaka till DBF-formatet för användning med äldre databasapplikationer.

{{% /alert %}}

## **Introduktion**

DBF (DataBase File) är ett äldre databasfilformat som ursprungligen introducerades av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande i stor utsträckning inom många branscher för att lagra strukturerad data, särskilt inom redovisning, GIS och andra specialiserade applikationer. Aspose.Cells låter dig integrera dessa äldre filer i moderna Java-kalkylbladsarbetsflöden sömlöst.

Biblioteket stöder både läsning och skrivning av DBF-filer, vilket ger dig möjlighet att:

- Importera data från befintliga DBF-filer till Aspose.Cells Workbook-objekt för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att omvandla data från andra kalkylbladsformat.
- Bibehålla fältdefinitioner, datatyper och poststrukturer vid överföring av data till och från DBF-formatet.

DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylbladsapplikationer, vilket gör dem till en bekväm brygga mellan äldre system och moderna kalkylbladsverktyg.

## **DBF-versioner och funktioner som stöds**

Aspose.Cells stöder följande DBF-formatversioner:

- **dBASE III** — Den ursprungliga och mest stödda varianten av DBF-formatet.
- **dBASE IV** — En utökad version som stöder ytterligare datatyper och större fältstorlekar.

### Funktioner som stöds

Biblioteket ger omfattande stöd för följande operationer:

- Läsa DBF-data till ett Workbook-objekt, med alla poster och fältdefinitioner bevarade.
- Skriva Workbook-data tillbaka till DBF-format för export till dBASE-kompatibla applikationer.
- Hantera vanliga datatyper som används i DBF-filer, inklusive tecken-, numeriska, datum- och logiska fält.
- Bevara fältdefinitioner som fältnamn, typ och längd under läs-/skrivoperationer.

### Begränsningar och överväganden

När du arbetar med DBF-filer bör du tänka på följande begränsningar:

- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 byte**.
- Fältnamn är begränsade till **10 tecken**, måste vara versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `YYYYMMDD`.
- Teckenkodning kan variera beroende på källapplikationen (vanligtvis Windows-1252 eller OEM-kodsidor).

## **Läsa en DBF-fil**

Aspose.Cells gör det enkelt att läsa in data från en DBF-fil till ett Workbook-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att data tolkas korrekt under inläsningsprocessen.

### Läsa en DBF-fil med Aspose.Cells

För att läsa en DBF-fil måste du skapa en `LoadOptions`-instans, ange dess `LoadFormat`-egenskap till `LoadFormat.Dbf` och skicka den till `Workbook`-konstruktören tillsammans med filsökvägen. När den är inläst blir data tillgänglig via samlingen `getWorksheets()`, där du kan iterera genom celler, extrahera värden eller manipulera data efter behov.

Följande exempel visar hur man läser in en befintlig DBF-fil i Aspose.Cells, kommer åt dess första Worksheet och läser cellvärdena.

```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "Data/";
String filePath = new File(new File(dataDir), "example.dbf").getPath();

LoadOptions loadOptions = new LoadOptions(LoadFormat.DBF);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

StringBuilder sb = new StringBuilder();

int maxRow = cells.getMaxDataRow();
int maxCol = cells.getMaxDataColumn();

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells.get(i, j);
        String value = cell.getStringValue();
        sb.append("|").append(value);
    }
    sb.append("|").append(System.lineSeparator());
}

System.out.println(sb.toString());

String outputPath = new File(new File(dataDir), "output.xlsx").getPath();
workbook.save(outputPath, SaveFormat.XLSX);

System.out.println("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel behandlar DBF-filen som ett kalkylblad och visar dess poster i en tabellayout. Detta är användbart för att snabbt verifiera data efter att ha läst eller skrivit den med Aspose.Cells.

{{% /alert %}}

## **Skriva en DBF-fil**

Att skriva data till en DBF-fil följer ett liknande mönster som att spara andra kalkylbladsformat med Aspose.Cells. Du skapar eller läser in en Workbook, fyller Worksheet med data och anropar sedan metoden `save` medan du anger `SaveFormat.Dbf` som målformat.

### Skriva en DBF-fil med Aspose.Cells

För att skapa en DBF-fil, följ dessa steg:

1. Skapa en ny `Workbook`-instans.
2. Öppna det första Worksheet från samlingen `getWorksheets()`.
3. Fyll Worksheet med dina data, inklusive rubriker i första raden och poster i efterföljande rader.
4. Anropa metoden `Workbook.save` och skicka filsökvägen och `SaveFormat.Dbf` som parametrar.

Följande exempel visar hur man skapar en ny DBF-fil från grunden. Det fyller ett Worksheet med exempeldata som innehåller olika datatyper (strängar, siffror och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

```java
import com.aspose.cells.*;
import java.io.File;
import java.util.GregorianCalendar;

String outputDir = "C:\\Output\\";
String filePath = new File(new File(outputDir), "output.dbf").getPath();

if (!new File(outputDir).exists())
{
    new File(outputDir).mkdirs();
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();

// Kolumnrubriker
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// Dat rad 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new GregorianCalendar(2020, 2, 15).getTime());

// Dat rad 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new GregorianCalendar(2019, 6, 22).getTime());

// Dat rad 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new GregorianCalendar(2021, 0, 10).getTime());

// Dat rad 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new GregorianCalendar(2018, 10, 5).getTime());

// Dat rad 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new GregorianCalendar(2022, 4, 30).getTime());

// Ställ in kolumnbredder för bättre läsbarhet
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, SaveFormat.DBF);
```

{{% alert color="primary" %}}

När du skriver data till en DBF-fil, se till att din data följer formatets begränsningar. Fältnamn bör inte vara längre än 10 tecken och får inte innehålla mellanslag. Poster som överstiger 4000 byte totalt kommer inte att sparas korrekt. Datum bör vara giltiga datumvärden som kan representeras i formatet `YYYYMMDD`.

{{% /alert %}}

## **Datatyp- och formateringsöverväganden**

Vid överföring av data mellan Aspose.Cells och DBF-formatet är det viktigt att förstå hur datatyper mappas mellan de två systemen för att säkerställa dataintegritet.

### Celltyper till DBF-fälttyper

Aspose.Cells-cellvärden konverteras automatiskt till lämpliga DBF-fälttyper vid sparande:

- **Strängar** mappas till teckenfält (C).
- **Numeriska värden** (heltal och decimaler) mappas till numeriska fält (N).
- **Datumvärden** mappas till datumfält (D) i formatet `YYYYMMDD`.
- **Booleska värden** mappas till logiska fält (L).

### Kodning

DBF-filer kan använda olika teckenkodningar beroende på applikationen som skapade dem. Aspose.Cells hanterar kodning transparent i de flesta fall, men om du stöter på problem med teckenvisning kan du behöva verifiera kodningen av källfilen.

### Regler för fältnamn

DBF-fältnamn måste följa följande regler:

- Maximal längd på 10 tecken.
- Måste börja med en bokstav.
- Får inte innehålla mellanslag eller specialtecken.
- Lagras som versaler oavsett skiftläge som används vid inmatning.

### Verifiera utdata

Efter att ha skrivit en DBF-fil kan du verifiera resultatet genom att öppna den i Microsoft Excel eller någon dBASE-kompatibel applikation. Data bör visas i en tabellayout med fältnamnen som kolumnrubriker, och posterna ifyllda enligt den data du angav.

## **Konvertera mellan DBF och andra format**

Ett av de mest praktiska användningsfallen för att läsa och skriva DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylbladsformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett brett utbud av format kan du enkelt läsa in en DBF-fil och spara om den i vilket annat som helst stött format, eller vice versa.

Till exempel kan du läsa en DBF-fil, tillämpa formatering eller beräkningar med Aspose.Cells-API:et och sedan spara resultatet som en XLSX-fil för distribution till användare som arbetar med moderna kalkylbladsapplikationer. Omvänt kan du ta data från en XLSX- eller CSV-fil och exportera den till DBF-format för integration med äldre system.



{{< app/cells/assistant language="java" >}}