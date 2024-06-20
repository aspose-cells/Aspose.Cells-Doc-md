---
title: Utiliser la fonctionnalité Annuler et Rétablir
type: docs
weight: 120
url: /fr/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop, annuler, rétablir
description: Cet article présente la fonctionnalité annuler et rétablir dans GridDesktop.
---

{{% alert color="primary" %}} 

La fonction Annuler/Rétablir de GridDesktop est très utile. Le nom explique sa fonctionnalité même, elle vous permet d'annuler/rétablir l'action ou les actions récentes dans une feuille de calcul. Par exemple, si une formule est supprimée accidentellement ou si vous modifiez des données dans une cellule que vous ne souhaitez pas réellement, ces actions peuvent être corrigées en utilisant les opérations Annuler et Rétablir fournies par le contrôle.

{{% /alert %}} 
## **Exécution de l'opération Annuler et Rétablir**
Les API suivantes sont disponibles pour la tâche. La description est donnée avec chaque API, veuillez les vérifier.

- **GridDesktop.EnableUndo** - attribut : Indique si la fonction Annuler est activée, la valeur par défaut est "false".
- **UndoManager** – classe : Elle est utilisée pour gérer l'opération Annuler/Rétablir.
- **GridDesktop.UndoManager** – attribut : Obtient l'instance de l'objet **UndoManager**.
- **UndoManager.Undo** – méthode : Effectue une opération Annuler.
- **UndoManager.Redo -** méthode : Effectue l'opération Rétablir.
- **UndoManager.ClearStack** – méthode : Efface la pile d'opérations Annuler/Rétablir.
- **UndoManager.UndoStepsCount** – attribut : Obtient le nombre d'étapes Annuler actuellement disponibles.
- **UndoManager.RedoStepsCount** – attribut : Obtient le nombre d'étapes Rétablir actuellement disponibles.
- **UndoManager.UndoStackSize** – attribut : Obtient/définit la taille de la pile Annuler.
### **Annuler**
Le code d'exemple suivant montre comment implémenter l'opération Annuler en utilisant l'API de GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Rétablir**
Le code d'exemple suivant montre comment implémenter l'opération Rétablir en utilisant l'API de GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Actuellement, l'opération Annuler/Rétablir fait référence au changement de la valeur d'une cellule.

{{% /alert %}}
