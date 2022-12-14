---
title: Libérer les ressources non gérées du classeur
type: docs
weight: 290
url: /fr/java/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}} 

 Aspose.Cells fournit[Classeur.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\) ) méthode pour libérer les ressources non managées du[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)objet. Le modèle de suppression est utilisé uniquement pour les objets qui accèdent aux ressources non managées, telles que les descripteurs de fichiers et de canaux, les descripteurs de registre, les descripteurs d'attente ou les pointeurs vers des blocs de mémoire non managée. En effet, le ramasse-miettes est très efficace pour récupérer les objets gérés inutilisés, mais il est incapable de récupérer les objets non gérés.

{{% /alert %}} 
## **Libérer les ressources non gérées du classeur**
L'exemple de code suivant montre comment utiliser le[Classeur.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
