---
title: Pourquoi pas l automatisation
type: docs
weight: 20
url: /fr/java/why-not-automation/
---

{{% alert color="primary" %}}

Pourquoi les composants Aspose sont-ils une bien meilleure option que l'automatisation de Microsoft Office ?*

Il y a deux questions que nous entendons le plus souvent ici chez Aspose :

1. **Vos produits nécessitent-ils que Microsoft Office soit installé pour fonctionner ?** 
   La réponse simple est non. Les composants Aspose sont totalement indépendants et ne sont pas affiliés à, ni autorisés, parrainés ou approuvés par Microsoft Corporation.
1. **Pourquoi devrions-nous utiliser les produits Aspose plutôt que d'utiliser l'automatisation de Microsoft Office ?**
   La réponse la plus courte que nous pourrions donner est qu'il y a de nombreuses raisons, la principale étant que Microsoft lui-même déconseille fortement l'automatisation Office à partir de solutions logicielles : [Considérations pour l'automatisation côté serveur d'Office](https://support.microsoft.com/fr-fr/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Il existe plusieurs raisons pour lesquelles les composants Aspose sont une meilleure alternative à l'automatisation. Certaines des principales raisons sont :

- [Sécurité](/cells/fr/java/why-not-automation/#security)
- [Stabilité](/cells/fr/java/why-not-automation/#security)
- [Scalabilité/Vitesse](/cells/fr/java/why-not-automation/#security)
- [Prix](/cells/fr/java/why-not-automation/#security)
- [Fonctionnalités](/cells/fr/java/why-not-automation/#security)

Les points clés sont décrits ci-dessous. Assurez-vous également de visiter les liens à la fin de cette section.

{{% /alert %}}

## **Sécurité**

Ce qui suit est une citation directe de l'article Microsoft ci-dessus mentionné : *"Les applications Office n'ont jamais été destinées à être utilisées côté serveur et, par conséquent, ne tiennent pas compte des problèmes de sécurité rencontrés par les composants distribués. Office n'authentifie pas les demandes entrantes et ne vous protège pas contre l'exécution involontaire de macros ou le démarrage d'un autre serveur qui pourrait exécuter des macros à partir de votre code côté serveur. Ne pas ouvrir les fichiers qui sont téléchargés sur le serveur à partir d'un site Web anonyme ! En fonction des paramètres de sécurité qui ont été définis en dernier, le serveur peut exécuter des macros sous un contexte Administrateur ou Système avec des privilèges complets et compromettre votre réseau ! De plus, Office utilise de nombreux composants côté client (comme Simple MAPI, WinInet et MSDAIPP) qui peuvent mettre en cache les informations d'authentification du client afin d'accélérer le traitement. Si Office est automatisé côté serveur, une instance peut servir plus d'un client, et parce que les informations d'authentification ont été mises en cache pour cette session, il est possible qu'un client utilise les informations d'identification mises en cache d'un autre client, et obtienne ainsi des permissions d'accès non accordées en usurpant d'autres utilisateurs."*

Les produits Aspose sont très sécurisés. Les composants Aspose s'exécutent dans le même contexte utilisateur que toutes les applications ASP.NET, sous l'utilisateur ASPNET. Par conséquent, les composants Aspose ne présentent pas de risque potentiel pour les ressources système vitales. De plus, lorsque qu’un document est ouvert par un composant Aspose, les macros ne sont pas exécutées automatiquement. Les composants Aspose ont été conçus dans le but de permettre aux développeurs de créer, manipuler et enregistrer des fichiers Office. Aucun des risques associés au package Microsoft Office n'est inhérent aux composants Aspose.

## **Stabilité**

Le passage suivant est une citation directe de l'article Microsoft susmentionné : *"Office 2000, Office XP et Office 2003 utilisent la technologie Microsoft Windows Installer (MSI) pour faciliter l'installation et l'auto-réparation pour un utilisateur final. MSI introduit le concept d'"installation au premier usage", qui permet aux fonctionnalités d'être installées ou configurées dynamiquement à l'exécution (pour le système, ou plus souvent pour un utilisateur spécifique). Dans un environnement côté serveur, cela ralentit les performances et augmente la probabilité qu'une boîte de dialogue puisse apparaître demandant à l'utilisateur d'approuver l'installation ou de fournir un disque d'installation approprié. Bien qu'il soit conçu pour augmenter la résilience de Office en tant que produit pour un utilisateur final, la mise en œuvre des capacités MSI de Office est contre-productive dans un environnement côté serveur. De plus, la stabilité de Office, en général, ne peut pas être garantie lorsqu'il est exécuté côté serveur car il n'a pas été conçu ou testé pour ce type d'utilisation. Utiliser Office en tant que composant de service sur un serveur réseau peut réduire la stabilité de cette machine et par conséquent de votre réseau dans son ensemble. Si vous prévoyez d'automatiser Office côté serveur, essayez d'isoler le programme sur un ordinateur dédié qui ne peut pas affecter les fonctions critiques et qui peut être redémarré selon les besoins."*

Comme les composants Aspose sont emballés dans un unique fichier DLL, il n'y aura jamais besoin d'installer des pièces ou des composants supplémentaires pour qu'ils fonctionnent. Les composants Aspose sont utilisés uniquement par les applications .NET et aucune partie du code du composant n'est conçue pour attendre une réponse humaine. Les composants Aspose ont été largement testés. Les composants Aspose sont utilisés par des entreprises telles qu'IBM, Hilton, Reader's Digest, Bank of America, et bien d'autres.

## **Scalabilité/Vitesse**

Le passage suivant est une citation directe de l'article Microsoft susmentionné : *"Les composants côté serveur doivent être des composants COM hautement réentrants et multi-thread avec un minimum de surcharge et un débit élevé pour de multiples clients. Les applications Office sont presque à tous égards le contraire exact. Elles sont non réentrantes, des serveurs d'automatisation basés sur STA conçus pour fournir une fonctionnalité diversifiée mais intensive en ressources pour un seul client. Elles offrent peu de scalabilité en tant que solution côté serveur et ont des limites fixées à des éléments importants, tels que la mémoire, qui ne peuvent pas être modifiés par la configuration. Plus important encore, elles utilisent des ressources globales (telles que des fichiers mappés en mémoire, des modules complémentaires ou modèles globaux, et des serveurs d'automatisation partagés), ce qui peut limiter le nombre d'instances pouvant s'exécuter simultanément et conduire à des conditions de concurrence si elles sont configurées dans un environnement multi-client. Les développeurs qui prévoient d'exécuter plusieurs instances de toute application Office en même temps doivent envisager une "mise en commun" ou une sérialisation de l'accès à l'application Office pour éviter les impasses potentielles ou la corruption des données."*

Les composants Aspose sont hautement évolutifs et extrêmement rapides. Les applications Office n'ont pas été conçues pour être utilisées simultanément par des centaines et des milliers d'utilisateurs ; cependant, les composants Aspose sont conçus précisément pour cela. Nos composants constituent une véritable solution .NET et fonctionnent parfaitement que ce soit sur un seul serveur au service d'une application unique ou sur une ferme web équilibrée au service d'une application d'entreprise à l'échelle.

## **Prix**

Lorsqu'une application utilise l'automatisation Microsoft Office, une copie de Microsoft Office doit être achetée pour chaque machine exécutant l'application. Il arrive souvent qu'une application ait besoin de créer ou de manipuler un fichier Office mais n'a pas besoin que l'utilisateur ait Office. Aspose offre une licence de redistribution très [économique](https://purchase.aspose.com/buy), sans redevance, qui permet un déploiement auprès d'un nombre illimité d'utilisateurs sans soucis de licence.

Lors de la création d'applications web, il est important de savoir que les composants d'automatisation Microsoft Office ne sont pas tarifés ni autorisés pour les solutions côté serveur ; par conséquent, il n'existe pas de bonne solution de licence pour le déploiement d'applications web utilisant les composants Microsoft Office. Aspose propose une solution très rentable pour les applications côté serveur également.

## **Fonctionnalités**

Les composants Aspose offrent tout ce dont vous avez besoin pour gérer les fichiers Office, et bien plus encore. Ils sont conçus avec la philosophie de permettre aux développeurs d'accomplir les meilleurs résultats avec le moins de travail possible. Contrairement à l'automatisation Office, les composants Aspose offrent de nombreuses fonctions puissantes et gain de temps. Par exemple, [Aspose.Cells](https://products.aspose.com/cells/java/) offre aux développeurs la possibilité d'exporter directement à partir d'un **DataTable** ou **DataView** dans un fichier Excel. [Chaque composant](https://products.aspose.com/total/) de la famille Aspose offre son propre ensemble de fonctionnalités uniques et puissantes.

La meilleure partie de l'achat d'un composant Aspose ou d'une suite de composants est d'avoir accès à nos équipes de développement. Nos équipes de développement comprennent que s'il existe une fonctionnalité dont votre entreprise a besoin, il est fort probable que d'autres entreprises en auront également besoin. Bien que toutes les demandes de fonctionnalités ne puissent être satisfaites, nos équipes essaient d'être très ouvertes et flexibles lorsqu'elles apportent leur aide. Cet état d'esprit a contribué à faire des composants Aspose ce qu'ils sont aujourd'hui. Si vous avez besoin de fonctionnalités supplémentaires des objets d'automatisation Office, vos chances de les voir ajoutés sont très, très faibles.

## **Conclusion**

{{% alert color="primary" %}}

Cet article a couvert les points clés pour lesquels les composants Aspose sont un meilleur choix que l'automatisation Office. Tous les différents composants Aspose offrent une version d'évaluation [sans risque ni obligation](https://products.aspose.com/total/). Nous vous encourageons à profiter de cette évaluation afin de mieux voir ce que Aspose peut apporter à vos applications.

Pour plus d'informations, consultez les articles Internet suivants :

- [Considérations pour l'automatisation côté serveur de Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
