---
title: Comment installer les polices TrueType sur Linux
type: docs
weight: 20
url: /fr/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

Le scénario le plus probable est que vous utilisez Aspose.Cells pour convertir des feuilles de calcul au format PDF. Si vous le faites sur un système d'exploitation autre que Windows, tel que Linux, ce sujet explique comment vous assurer qu'Aspose.Cells rend vos feuilles de calcul avec la meilleure fidélité.

Pour vous assurer que les feuilles de calcul converties par Aspose.Cells apparaissent aussi fidèlement que possible à l'original, vous devrez peut-être installer des « polices de Windows » ou des « polices TrueType » sur votre système Linux car les polices TrueType les plus couramment utilisées ne sont pas préinstallées par défaut dans les distributions Linux.

Il existe deux moyens principaux d'obtenir des polices TrueType sur un système Linux :

1. Copier les fichiers de polices (.TTF et .TTC) d'une machine Windows vers votre machine Linux.
1. Installer un package de polices TrueType, tel que msttcorefonts.

{{% /alert %}}

## **Copiez les polices d'un ordinateur sous Windows**

Une façon simple et rapide est de copier les fichiers .TTF et .TTC du répertoire C:\Windows\Fonts d'un ordinateur sous Windows vers un répertoire sur votre ordinateur sous Linux. Vous n'avez pas besoin d'installer ou d'enregistrer ces polices sur Linux de quelque manière que ce soit, il vous suffit de spécifier l'emplacement des polices en utilisant la méthode FontConfigs.setFontFolder dans votre application.

{{% alert color="primary" %}}

Autant que nous puissions dire, Microsoft accorde des licences pour les polices afin que tout le monde puisse les utiliser librement, mais veuillez vérifier par vous-même la licence des polices.

{{% /alert %}}

## **Installer un package de polices TrueType**

Les informations fournies ci-dessous vous guideront pas à pas pour installer les polices TrueType les plus célèbres de Microsoft sur des distributions Linux telles que Fedora et Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Vous pouvez avoir besoin de privilèges de niveau 'root', donc connectez-vous en tant que 'root' ou configurez sudo.

{{% /alert %}}

Voici comment faire à l'aide du Terminal.

1. Assurez-vous d'avoir les packages RPM suivants installés.
   1. **rpm-build** : Si ce n'est pas installé, utilisez la commande suivante pour installer le package rpm-build

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget** : Si ce n'est pas installé, utilisez la commande suivante

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. Téléchargez le dernier fichier spec msttcorefonts depuis SourceForge en utilisant la commande suivante,

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Construisez un fichier RPM en utilisant le fichier spec précédemment téléchargé et la commande suivante,

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Le fichier RPM sera stocké dans : /root/rpmbuild/RPMS/noarch/, installez-le comme suit,

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Redémarrez la machine pour que les changements prennent effet.

Les instructions ci-dessus permettront d'installer le package de polices Microsoft TTFs comprenant les familles de polices suivantes :

1. Andale Mono
1. Arial Black/Arial (Gras, Italique, Gras Italique)
1. Comic Sans MS (Gras)
1. Courier New (Gras, Italique, Gras Italique)
1. Georgia (Gras, Italique, Gras Italique)
1. Impact
1. Tahoma
1. Times New Roman (Gras, Italique, Gras Italique)
1. Trebuchet (Gras, Italique, Gras Italique)
1. Verdana (Gras, Italique, Gras Italique)
1. Webdings

{{% alert color="primary" %}}

Sur Ubuntu, allez dans le Gestionnaire de paquets Synaptic. Trouvez et installez le paquet **ttf-mscorefonts-installer**.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
