---
title: Använda funktionen Ångra och Gör om
type: docs
weight: 120
url: /sv/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

GridDesktops Ångra/Gör om-funktion är mycket användbar. Namnet förklarar själva dess funktionalitet, det låter dig ångra/göra om de senaste åtgärderna i ett kalkylblad. Till exempel, om en formel raderas av misstag eller om du redigerar data i en cell som du egentligen inte vill ha, kan dessa åtgärder korrigeras genom att använda Ångra- och Gör om-operationerna som tillhandahålls av kontrollen.

{{% /alert %}} 
## **Utför Ångra och Gör om**
Följande API:er är tillgängliga för uppgiften. Beskrivningen ges med varje API, kontrollera dem.

- **GridDesktop.EnableUndo** - attribut: Det indikerar om funktionen Ångra är aktiverad, standardvärdet är "falskt".
- **UndoManager** – klass: Den används för att hantera operationen ångra/gör om.
- **GridDesktop.UndoManager** – attribut: Den får instansen av**UndoManager** objekt.
- **UndoManager.Ångra** – metod: Den utför en ångra-operation.
- **UndoManager.Redo -** metod: Den utför redo-operationen.
- **UndoManager.ClearStack** – metod: Den rensar ångra/gör om-stacken.
- **UndoManager.UndoStepsCount** – attribut: Den får räkningen av aktuella tillgängliga ångra steg.
- **UndoManager.RedoStepsCount** – attribut: Den får räkningen av aktuella tillgängliga redo-steg.
- **UndoManager.UndoStackSize** – attribut: Den får/ställer in storleken på ångra stack.
### **Ångra**
Följande exempelkod visar hur man implementerar Ångra-operationen med GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Göra om**
Följande exempelkod visar hur man implementerar Redo-operationen med GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

För närvarande avser ångra/gör om ändringen av ett cellvärde.

{{% /alert %}}
