---
title: Configuration des démos
type: docs
weight: 40
url: /fr/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

Aspose.Cells pour JasperReports comprend un certain nombre de projets de démonstration pour vous aider à commencer à exporter des rapports vers les formats de document Excel Microsoft à partir de votre application.

Les démos fournies avec Aspose.Cells pour JasperReports sont des démos JasperReports standard modifiées pour démontrer l'utilisation des nouveaux exportateurs.

{{% /alert %}}

Pour exécuter Aspose.Cells pour les démos JasperReports, procédez comme suit :

1.  Télécharger JasperReports (par exemple<https://sourceforge.net/projects/jasperreports/files/archive/>). Assurez-vous de télécharger l'intégralité du projet archivé avec le code source et les démos, pas seulement un seul JAR.
1. Décompressez le projet archivé à un emplacement sur votre disque dur, par exemple C:\.
1.  Copiez tous les dossiers de démonstration du dossier \demo de**Aspose.Cells.JasperReports.zip** à**\<InstallDir>\demo\samples**, où "\<InstallDir>" est l'emplacement dans lequel vous avez décompressé JasperReports. Cette étape est nécessaire car les scripts de construction de démonstration reposent sur la structure de dossiers de JasperReports, sinon vous devrez modifier les scripts de construction.
1.  Copie**aspose.cells.jasperreports.jar** du dossier \lib de Aspose.Cells.JasperReports.zip vers**\<InstallDir>\lib**.
1.  Préparez Ant Build Tool et Ivy Dependency Manager, voir**\<InstallDir>\readme.txt**.
1.  Modifier le**build.xml** à**\<InstallDir>\demo\samples**, ajoutez aspose.cells.jasperreports.jar dans le classpath :
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. Changer le répertoire courant en**\<InstallDir>\demo\hsqldb** et exécutez la ligne de commande suivante :
   **fourmi runServer**
1.  Remplacez le répertoire actuel par l'un des Aspose.Cells pour les démos JasperReports, par exemple**\<InstallDir>\demo\samples\ac.charts** et exécutez les commandes suivantes dans la ligne de commande :
   **test de fourmi** - de produire des fichiers de rapport à l'aide de l'exportateur XLS Aspose.
1.  Ouvrez l'un des documents résultants pour afficher, par exemple**\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** dans Microsoft Excel ou une autre application.
