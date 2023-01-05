---
title: Hantera kommentarer i arbetsblad
type: docs
weight: 110
url: /sv/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

Det här ämnet diskuterar att lägga till, komma åt och ta bort kommentarer från kalkylblad. Kommentarer är användbara för att lägga till anteckningar eller användbar information för användare som ska arbeta med arket. Utvecklare har flexibiliteten att lägga till kommentarer till valfri cell i kalkylbladet.

{{% /alert %}} 
## **Arbeta med kommentarer**
### **Lägger till kommentarer**
För att lägga till en kommentar till arbetsbladet, följ stegen nedan:

1. Lägg till kontrollen Aspose.Cells.GridWeb i webbformuläret.
1. Öppna kalkylbladet du lägger till kommentarer till.
1. Lägg till en kommentar till en cell.
1. Ange en anteckning för den nya kommentaren.

**En kommentar har lagts till i arbetsbladet** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Åtkomst till kommentarer**
För att komma åt en kommentar:

1. Öppna cellen som innehåller kommentaren.
1. Få cellens referens.
1. Skicka referensen till kommentarsamlingen för att komma åt kommentaren.
1. Det är nu möjligt att ändra kommentarens egenskaper.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Ta bort kommentarer**
Så här tar du bort en kommentar:

1. Gå till cellen enligt beskrivningen ovan.
1. Använd kommentarsamlingens RemoveAt-metod för att ta bort kommentaren.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
