---
title: Hantera kommentarer i kalkylblad
type: docs
weight: 110
url: /sv/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: Denna artikel visar hur man arbetar med kommentarer i GridWeb.
---

{{% alert color="primary" %}} 

Detta ämne diskuterar tillägg, åtkomst och borttagning av kommentarer från arbetsblad. Kommentarer är användbara för att lägga till anteckningar eller användbar information för användare som kommer att arbeta med arket. Utvecklare har flexibiliteten att lägga till kommentarer till valfri cell i arbetsbladet.

{{% /alert %}} 
## **Arbeta med kommentarer**
### **Lägga till kommentarer**
För att lägga till en kommentar i arbetsbladet, följ stegen nedan:

1. Lägg till kontrollen Aspose.Cells.GridWeb till webbformuläret.
1. Gå till det arbetsblad där du ska lägga till kommentarer.
1. Lägg till en kommentar i en cell.
1. Ange en anteckning för den nya kommentaren.

**En kommentar har lagts till i arbetsbladet** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Åtkomst till kommentarer**
För att komma åt en kommentar:

1. Gå till den cell som innehåller kommentaren.
1. Hämta cellens referens.
1. Skicka referensen till kommentarsamlingen för att komma åt kommentaren.
1. Det är nu möjligt att ändra kommentarens egenskaper.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Ta bort kommentarer**
För att ta bort en kommentar:

1. Gå till cellen som förklarats ovan.
1. Använd kommentarsamlingens RemoveAt-metod för att ta bort kommentaren.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
