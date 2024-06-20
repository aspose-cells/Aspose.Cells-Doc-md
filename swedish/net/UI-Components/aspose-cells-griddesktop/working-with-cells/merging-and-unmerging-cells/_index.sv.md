---
title: Sammanfoga och avsammanfoga celler i GridDesktop
linktitle: Sammanfoga och dela upp celler
type: docs
weight: 90
url: /sv/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop, sammanfoga, avsammanfoga
description: Den här artikeln introducerar sammanfoga och avsammanfoga i GridDesktop.
---

{{% alert color="primary" %}} 

I det här avsnittet kommer vi att diskutera en nyttig funktion för att sammanfoga och avsammanfoga celler i ett kalkylblad. Den här funktionen är användbar i de fall när vi behöver spänna några rader eller kolumner för att förbättra läsbarheten av data.

{{% /alert %}} 
## **Sammanfoga celler**
För att sammanfoga celler till en enda stor cell, följ stegen nedan:

- Kom åt något önskat **Kalkylblad**
- Skapa en **CellRange** att sammanfoga
- **Sammanfoga** cellområdet till en stor cell

Du kan använda **Merge** metoden av **Worksheet** för att sammanfoga celler. Men en rad celler kan definieras med hjälp av **CellRange** objekt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Avmarkera celler**
För att avmarkera en stor cell till många celler, följ stegen nedan:

- Kom åt något önskat **Kalkylblad**
- Öppna den sammanfogade cellen som behöver avmarkeras
- **Avmarkera** den stora cellen till många celler med hjälp av platsen för den sammanfogade cellen

Du kan använda **Avmarkera** metoden av **Worksheet** för att avmarkera en cell med dess plats.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

När du sammanfogar celler till en enda cell tillämpas formateringsinställningarna för den översta vänstra cellen (i cellintervallet) på den sammanfogade cellen, men när cellen avmarkeras behåller alla avmarkerade celler sina formateringsinställningar.

{{% /alert %}}
