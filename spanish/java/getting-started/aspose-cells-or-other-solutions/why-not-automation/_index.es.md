---
title: ¿Por qué no la Automatización
type: docs
weight: 20
url: /es/java/why-not-automation/
---

{{% alert color="primary" %}}

¿Por qué son los componentes de Aspose una opción mucho mejor que la Automatización de Microsoft Office?

Hay dos preguntas que escuchamos con más frecuencia aquí en Aspose:

1. **¿Tus productos requieren que Microsoft Office esté instalado para que funcionen?** 
   La respuesta simple es no. Los componentes de Aspose son totalmente independientes y no están afiliados, ni autorizados, patrocinados o aprobados por Microsoft Corporation.
1. **¿Por qué deberíamos usar los productos de Aspose en lugar de utilizar la automatización de Microsoft Office?**
   La respuesta más breve que podríamos dar es que hay muchas razones, siendo la principal que Microsoft en sí mismo desaconseja fuertemente la automatización de Office desde soluciones de software: [Considerations for server-side Automation of Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Hay varias razones por las cuales los componentes de Aspose son una mejor alternativa a la automatización. Algunas de las razones clave son:

- [Seguridad](/cells/es/java/why-not-automation/#security)
- [Estabilidad](/cells/es/java/why-not-automation/#security)
- [Escalabilidad/Velocidad](/cells/es/java/why-not-automation/#security)
- [Precio](/cells/es/java/why-not-automation/#security)
- [Características](/cells/es/java/why-not-automation/#security)

Los puntos clave se describen a continuación. Además, asegúrese de visitar los enlaces al final de esta sección.

{{% /alert %}}

## **Seguridad**

La siguiente es una cita directa del artículo de Microsoft antes mencionado: *"Las aplicaciones de Office nunca fueron destinadas para uso en el servidor, por lo que no tienen en cuenta los problemas de seguridad que enfrentan los componentes distribuidos. Office no autentica las solicitudes entrantes y no le protege de ejecutar macros de forma no intencional, o iniciar otro servidor que pudiera ejecutar macros, desde su código del lado del servidor. ¡No abra archivos que se carguen en el servidor desde un sitio web anónimo! Basado en la configuración de seguridad que se estableció por última vez, ¡el servidor puede ejecutar macros bajo el contexto de un administrador o del sistema con todos los privilegios y comprometer su red! Además, Office utiliza muchos componentes del lado del cliente (como Simple MAPI, WinInet y MSDAIPP) que pueden almacenar en caché la información de autenticación del cliente para acelerar el procesamiento. Si Office se está automatizando del lado del servidor, una instancia puede atender a más de un cliente, y debido a que la información de autenticación se ha almacenado en caché para esa sesión, es posible que un cliente pueda usar las credenciales en caché de otro cliente, y así obtener permisos de acceso no autorizados al suplantar a otros usuarios."*

Los productos de Aspose son muy seguros. Los componentes de Aspose se ejecutan en el mismo contexto de usuario que todas las aplicaciones ASP.NET, bajo el usuario ASPNET. Por lo tanto, los componentes de Aspose no representan un riesgo potencial para los recursos del sistema vital. Además, cuando un documento es abierto por un componente de Aspose, las macros no se ejecutan automáticamente. Los componentes de Aspose fueron construidos con el objetivo de permitir a los desarrolladores crear, manipular y guardar archivos de Office. Ninguno de los riesgos asociados con el paquete de Microsoft Office son inherentes a los componentes de Aspose.

## **Estabilidad**

La siguiente es una cita directa del artículo de Microsoft antes mencionado: *"Office 2000, Office XP y Office 2003 utilizan la tecnología Microsoft Windows Installer (MSI) para facilitar la instalación y autorreparación para un usuario final. MSI introduce el concepto de "instalar al usar por primera vez", que permite instalar o configurar dinámicamente características en tiempo de ejecución (para el sistema, o con mayor frecuencia para un usuario particular). En un entorno del lado del servidor, esto ralentiza el rendimiento y aumenta la probabilidad de que aparezca un cuadro de diálogo que solicite al usuario aprobar la instalación o proporcione un disco de instalación adecuado. Aunque está diseñado para aumentar la capacidad de recuperación de Office como producto para el usuario final, la implementación de las capacidades de MSI de Office es contraproducente en un entorno del lado del servidor. Además, la estabilidad de Office, en general, no se puede garantizar al ejecutarse del lado del servidor porque no ha sido diseñado ni probado para este tipo de uso. El uso de Office como un componente de servicio en un servidor de red puede reducir la estabilidad de esa máquina y como consecuencia, la estabilidad de su red en su conjunto. Si planea automatizar Office del lado del servidor, intente aislar el programa en una computadora dedicada que no pueda afectar funciones críticas y que pueda reiniciarse según sea necesario."*

Dado que los componentes de Aspose están empaquetados en un solo DLL, nunca habrá necesidad de instalar partes o piezas adicionales para que funcionen. Los componentes de Aspose son utilizados solo por aplicaciones .NET y no hay ninguna parte del código del componente diseñada para esperar una respuesta humana. Los componentes de Aspose han sido ampliamente probados. Las empresas como IBM, Hilton, Reader's Digest, Bank of America y muchas más utilizan los componentes de Aspose.

## **Escalabilidad/Velocidad**

La siguiente es una cita directa del artículo de Microsoft antes mencionado: *"Los componentes del lado del servidor deben ser componentes COM altamente reentrantes y con subprocesos múltiples con un mínimo sobrecarga y alto rendimiento para múltiples clientes. Las aplicaciones de Office son en casi todos los aspectos lo opuesto exacto. Son servidores de automatización basados en STA no reentrantes diseñados para proporcionar funcionalidad diversa pero intensiva en recursos para un único cliente. Ofrecen poca escalabilidad como solución del lado del servidor y tienen límites fijos en elementos importantes, como la memoria, que no se pueden cambiar a través de la configuración. Más importante aún, utilizan recursos globales (como archivos de mapa de memoria, complementos o plantillas globales y servidores de automatización compartidos), que pueden limitar el número de instancias que pueden ejecutarse simultáneamente y provocar condiciones de carrera si se configuran en un entorno multi-cliente. Los desarrolladores que planean ejecutar más de una instancia de cualquier aplicación de Office al mismo tiempo necesitan considerar "agrupar" o serializar el acceso a la aplicación de Office para evitar posibles bloqueos de recursos o corrupción de datos."*

Los componentes de Aspose son altamente escalables y rápidos. Las aplicaciones de Office no fueron diseñadas para ser utilizadas simultáneamente por cientos y miles de usuarios; sin embargo, los componentes de Aspose están diseñados para eso. Nuestros componentes son una solución .NET verdadera y funcionan a la perfección ya sea en un solo servidor que alimenta una única aplicación o en una granja web equilibrada que alimenta una aplicación empresarial a nivel de empresa.

## **Precio**

Cuando una aplicación utiliza la automatización de Microsoft Office, se debe comprar una copia de Microsoft Office para cada máquina que ejecute la aplicación. En muchas ocasiones, una aplicación puede necesitar crear o manipular un archivo de Office pero no requiere que el usuario tenga Office. Aspose ofrece una licencia de [redistribución](https://purchase.aspose.com/buy) muy rentable y libre de regalías que permitirá la implementación a un número ilimitado de usuarios sin preocupaciones de licencia.

Al crear aplicaciones basadas en web, es importante saber que los componentes de la automatización de Microsoft Office no tienen precio ni licencia para soluciones del lado del servidor; por lo tanto, no hay una buena solución de licencias para implementar aplicaciones web que utilicen los componentes de Microsoft Office. Aspose ofrece una solución muy rentable para aplicaciones basadas en servidor también.

## **Características**

Los componentes de Aspose proporcionan todo lo necesario para administrar archivos de Office, y mucho más. Están diseñados con la filosofía de permitir a los desarrolladores lograr los mejores resultados con la menor cantidad de trabajo. A diferencia de la automatización de Office, los componentes de Aspose proporcionan muchas funciones poderosas que ahorran tiempo. Por ejemplo, [Aspose.Cells](https://products.aspose.com/cells/java/) ofrece a los desarrolladores la capacidad de exportar directamente desde un **DataTable** o **DataView** a un archivo de Excel. [Cada componente](https://products.aspose.com/total/) en la familia de Aspose ofrece su propio conjunto de características únicas y poderosas.

La mejor parte de comprar un componente de Aspose o un conjunto de componentes es tener acceso a nuestros equipos de desarrollo. Nuestros equipos de desarrollo se dan cuenta de que si hay una característica que su empresa necesita, muy probablemente otras empresas también la necesitarán. Si bien no todas las solicitudes de características pueden ser agregadas, nuestros equipos intentan ser muy abiertos y flexibles al brindar asistencia. Esa mentalidad es lo que ha ayudado a los componentes de Aspose a convertirse en tan poderosos como son. Si hay características adicionales que necesita de los objetos de automatización de Office, sus posibilidades de tenerlas agregadas son muy, muy bajas.

## **Conclusión**

{{% alert color="primary" %}}

Este artículo ha cubierto los puntos clave sobre por qué los componentes de Aspose son una mejor opción que la automatización de Office. Todos los diferentes componentes de Aspose ofrecen una versión de evaluación sin riesgos ni obligaciones. Le animamos a aprovechar esa evaluación para ver mejor lo que Aspose puede hacer por sus aplicaciones.

Para obtener más información, consulte los siguientes artículos en Internet:

- [Consideraciones para la automatización del lado del servidor de Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
