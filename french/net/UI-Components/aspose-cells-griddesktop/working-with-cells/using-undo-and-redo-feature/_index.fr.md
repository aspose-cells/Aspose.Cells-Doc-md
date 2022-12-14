---
title: Utilisation de la fonction Annuler et Rétablir
type: docs
weight: 120
url: /fr/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

La fonctionnalité Undo/Redo de GridDesktop est très utile. Le nom explique sa fonctionnalité elle-même, il vous permet d'annuler/rétablir la ou les actions récentes dans une feuille de calcul. Par exemple, si une formule est accidentellement supprimée ou si vous modifiez des données dans une cellule dont vous ne voulez pas réellement, ces actions peuvent être corrigées en utilisant les opérations Annuler et Rétablir fournies par le contrôle.

{{% /alert %}} 
## **Exécution de l'opération Annuler et Rétablir**
Les API suivantes sont disponibles pour la tâche. La description est donnée avec chaque API, veuillez les vérifier.

- **GridDesktop.EnableUndoGridDesktop.EnableUndo** - attribut : Il indique si la fonction Undo est activée, la valeur par défaut est "false".
- **UndoManager** – classe : Elle est utilisée pour gérer l'opération undo/redo.
- **GridDesktop.UndoManagerGridDesktop.UndoManager** – attribut : il obtient l'instance de**UndoManager** objet.
- **UndoManager.Undo** – méthode : elle effectue une opération d'annulation.
- **UndoManager.Redo -** méthode : elle effectue l'opération de rétablissement.
- **UndoManager.ClearStack** – méthode : elle efface la pile d'annulation/rétablissement.
- **UndoManager.UndoStepsCountUndoManager.UndoStepsCount** – attribut : il obtient le nombre d'étapes d'annulation actuellement disponibles.
- **UndoManager.RedoStepsCount** – attribut : il obtient le nombre d'étapes de rétablissement actuellement disponibles.
- **UndoManager.UndoStackSize** – attribut : il obtient/définit la taille de la pile d'annulation.
### **annuler**
L'exemple de code suivant montre comment implémenter l'opération Annuler à l'aide de GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Refaire**
L'exemple de code suivant montre comment implémenter l'opération Redo à l'aide de GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Actuellement, l'opération annuler/rétablir fait référence à la modification de la valeur d'une cellule.

{{% /alert %}}
