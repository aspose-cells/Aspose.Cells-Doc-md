---
title: Libérer les ressources non gérées du classeur
type: docs
weight: 310
url: /fr/net/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit[**Classeur.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) méthode pour libérer les ressources non managées du[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)objet. Le modèle de suppression est utilisé uniquement pour les objets qui accèdent aux ressources non managées, telles que les descripteurs de fichiers et de canaux, les descripteurs de registre, les descripteurs d'attente ou les pointeurs vers des blocs de mémoire non managée. En effet, le ramasse-miettes est très efficace pour récupérer les objets gérés inutilisés, mais il est incapable de récupérer les objets non gérés.

{{% /alert %}}

[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) objet implémente maintenant le*System.IDisposable* interface qui a une seule méthode[**Disposer()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) . Vous pouvez soit appeler directement le[**Classeur.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) méthode ou vous pouvez utiliser la*En utilisant*instruction pour appeler cette méthode automatiquement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
