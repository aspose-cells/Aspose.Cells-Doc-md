---
title: Använd Ångra och Gör om funktionen
type: docs
weight: 120
url: /sv/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop, ångra, gör om
description: Denna artikel introducerar undo och redo funktionen i GridDesktop.
---

{{% alert color="primary" %}} 

GridDesktop's Ångra/Gör om-funktion är mycket användbar. Namnet förklarar dess funktion själv, det låter dig ångra/göra om de senaste åtgärderna i ett kalkylblad. Till exempel, om en formel av misstag raderas eller om du redigerar data i en cell som du egentligen inte vill, kan dessa åtgärder rättas till genom att använda Ångra och Gör om-operationerna som tillhandahålls av kontrollen.

{{% /alert %}} 
## **Genomför Undo- och Redo-åtgärd**
Följande API:er är tillgängliga för uppgiften. Beskrivningen ges med varje API, var god kontrollera dem.

- **GridDesktop.EnableUndo** - attribut: Det indikerar om Undo-funktionen är aktiverad, standardvärdet är "false".
- **UndoManager** – klass: Det används för att hantera undo/redo-åtgärden.
- **GridDesktop.UndoManager** – attribut: Det hämtar instansen av **UndoManager**-objektet.
- **UndoManager.Undo** – metod: Det utför en undo-åtgärd.
- **UndoManager.Redo** – metod: Det utför redo-åtgärden.
- **UndoManager.ClearStack** – metod: Det rensar undo/redo-stacken.
- **UndoManager.UndoStepsCount** – attribut: Det hämtar antalet tillgängliga undo-steg.
- **UndoManager.RedoStepsCount** – attribut: Det hämtar antalet tillgängliga redo-steg.
- **UndoManager.UndoStackSize** – attribut: Det hämtar/sätter storleken på undo-stacken.
### **Ångra**
Följande exemplarkod visar hur man implementerar Undo-åtgärden med hjälp av GridDesktop API:n.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Gör om**
Följande exemplarkod visar hur man implementerar Redo-åtgärden med hjälp av GridDesktop API:n.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

För närvarande hänvisar ångra/gör om-åtgärden till ändringen av en cellvärde.

{{% /alert %}}
