---
title: Libérer les ressources non gérées du classeur
type: docs
weight: 310
url: /fr/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells fournit la méthode [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) pour libérer les ressources non managées de l'objet [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Le modèle de libération est utilisé uniquement pour les objets qui accèdent à des ressources non managées, telles que des poignées de fichiers et de tubes, des poignées de registre, des poignées d'attente ou des pointeurs vers des blocs de mémoire non gérée. C'est parce que le collecteur de vidanges est très efficace pour récupérer les objets managés inutilisés, mais qu'il est incapable de récupérer les objets non managés.

{{% /alert %}}

L'objet [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) implémente maintenant l'interface *System.IDisposable* qui a une seule méthode [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose). Vous pouvez soit appeler directement la méthode [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose), soit utiliser l'instruction *Using* pour appeler automatiquement cette méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
{{< app/cells/assistant language="csharp" >}}
