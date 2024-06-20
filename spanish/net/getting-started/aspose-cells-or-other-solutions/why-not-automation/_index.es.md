---
title: ¿Por qué no la Automatización
type: docs
weight: 50
url: /es/net/why-not-automation/
---

{{% alert color="primary" %}}

¿Por qué son los componentes de Aspose una opción mucho mejor que la Automatización de Microsoft Office?

{{% /alert %}}

## **Introducción**

Hay dos preguntas que escuchamos con más frecuencia aquí en Aspose:

1. **¿Tus productos requieren que Microsoft Office esté instalado para que funcionen?**
   La respuesta simple es no. Los componentes de Aspose son totalmente independientes y no están afiliados, ni autorizados, patrocinados o aprobados por Microsoft Corporation.
1. **¿Por qué deberíamos usar los productos de Aspose en lugar de utilizar la automatización de Microsoft Office?**
   La respuesta más breve que podríamos dar es que hay muchas razones, siendo la principal que Microsoft en sí mismo desaconseja fuertemente la automatización de Office desde soluciones de software: [Considerations for server-side Automation of Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Hay varias razones por las cuales los componentes de Aspose son una mejor alternativa a la automatización. Algunas de las razones clave son:

- Seguridad
- Estabilidad
- Escalabilidad/Velocidad
- Precio
- Funcionalidades

Los puntos clave se describen a continuación. Además, asegúrese de visitar los enlaces al final de esta sección.

### **Seguridad**

Lo siguiente es una cita directa del artículo de Microsoft mencionado anteriormente:

*"Las aplicaciones de Office nunca fueron concebidas para ser usadas del lado del servidor, y por lo tanto no tienen en cuenta los problemas de seguridad a los que se enfrentan los componentes distribuidos. Office no autentica las solicitudes entrantes y no lo protege de ejecutar accidentalmente macros, o iniciar otro servidor que pueda ejecutar macros, desde su código del lado del servidor. ¡No abra archivos que se carguen en el servidor desde un sitio web anónimo! Basado en la configuración de seguridad que se estableció por última vez, el servidor puede ejecutar macros bajo un contexto de Administrador o Sistema con privilegios completos, y comprometer su red. Además, Office utiliza muchos componentes del lado del cliente (como Simple MAPI, WinInet y MSDAIPP) que pueden almacenar en caché información de autenticación del cliente para acelerar el procesamiento. Si Office se está automatizando del lado del servidor, una instancia puede atender a más de un cliente, y debido a que se ha almacenado en caché la información de autenticación para esa sesión, es posible que un cliente pueda utilizar las credenciales en caché de otro cliente, y por lo tanto obtener permisos de acceso no concedidos al suplantar a otros usuarios."*

Los productos de Aspose son muy seguros. Los componentes de Aspose se ejecutan en el mismo contexto de usuario que todas las aplicaciones ASP.NET, bajo el usuario ASPNET. Por lo tanto, los componentes de Aspose no representan un riesgo potencial para los recursos del sistema vital. Además, cuando un documento es abierto por un componente de Aspose, las macros no se ejecutan automáticamente. Los componentes de Aspose fueron construidos con el objetivo de permitir a los desarrolladores crear, manipular y guardar archivos de Office. Ninguno de los riesgos asociados con el paquete de Microsoft Office son inherentes a los componentes de Aspose.

### **Estabilidad**

Lo siguiente es una cita directa del artículo de Microsoft mencionado anteriormente:

*"Office 2000, Office XP y Office 2003 utilizan la tecnología de Windows Installer (MSI) de Microsoft para facilitar la instalación y auto-reparación para el usuario final. MSI introduce el concepto de "instalar al usar por primera vez", lo que permite que las características se instalen o configuren dinámicamente en tiempo de ejecución (para el sistema, o más a menudo para un usuario particular). En un entorno de servidor, esto ralentiza el rendimiento y aumenta la probabilidad de que aparezca un cuadro de diálogo que pida al usuario que apruebe la instalación o proporcione un disco de instalación apropiado. Aunque está diseñado para aumentar la capacidad de recuperación de Office como producto para el usuario final, la implementación de las capacidades de MSI de Office es contraproducente en un entorno de servidor. Además, la estabilidad de Office, en general, no se puede asegurar al ejecutar en el lado del servidor porque no ha sido diseñado ni probado para este tipo de uso. Utilizar Office como un componente de servicio en un servidor de red puede reducir la estabilidad de esa máquina y, como consecuencia, de toda su red. Si planea automatizar Office en el lado del servidor, intente aislar el programa en una computadora dedicada que no pueda afectar funciones críticas y que pueda reiniciarse según sea necesario."*

Dado que los componentes de Aspose están empaquetados en un solo DLL, nunca habrá necesidad de instalar partes o piezas adicionales para que funcionen. Los componentes de Aspose son utilizados solo por aplicaciones .NET y no hay ninguna parte del código del componente diseñada para esperar una respuesta humana. Los componentes de Aspose han sido ampliamente probados. Las empresas como IBM, Hilton, Reader's Digest, Bank of America y muchas más utilizan los componentes de Aspose.

### **Escalabilidad/Velocidad**

Lo siguiente es una cita directa del artículo de Microsoft mencionado anteriormente:

*"Los componentes del lado del servidor necesitan ser componentes COM multi-hilos altamente reentrantes con un mínimo sobrecarga y alto rendimiento para múltiples clientes. Las aplicaciones de Office son en casi todos los aspectos exactamente lo opuesto. No son reentrantes, servidores de automatización basados en STA que están diseñados para proporcionar funcionalidades diversas pero intensivas en recursos para un solo cliente. Ofrecen poca escalabilidad como solución del lado del servidor y tienen límites fijos en elementos importantes, como la memoria, que no se pueden cambiar mediante configuración. Más importante aún, utilizan recursos globales (como archivos mapeados en memoria, complementos o plantillas globales, y servidores de automatización compartidos), lo que puede limitar el número de instancias que pueden ejecutarse simultáneamente y provocar condiciones de carrera si se configuran en un entorno multi-cliente. Los desarrolladores que planean ejecutar más de una instancia de cualquier aplicación de Office al mismo tiempo deben considerar "agrupar" o serializar el acceso a la aplicación de Office para evitar posibles bloqueos o corrupción de datos."*

Los componentes de Aspose son altamente escalables y rápidos. Las aplicaciones de Office no fueron diseñadas para ser utilizadas simultáneamente por cientos y miles de usuarios; sin embargo, los componentes de Aspose están diseñados para eso. Nuestros componentes son una solución .NET verdadera y funcionan a la perfección ya sea en un solo servidor que alimenta una única aplicación o en una granja web equilibrada que alimenta una aplicación empresarial a nivel de empresa.

### **Precio**

Cuando una aplicación utiliza la automatización de Microsoft Office, se debe comprar una copia de Microsoft Office para cada máquina que ejecute la aplicación. En muchas ocasiones, una aplicación puede necesitar crear o manipular un archivo de Office pero no requiere que el usuario tenga Office. Aspose ofrece una licencia de [redistribución](https://purchase.aspose.com/buy) muy rentable y libre de regalías que permitirá la implementación a un número ilimitado de usuarios sin preocupaciones de licencia.

Al crear aplicaciones basadas en la web, es importante saber que los componentes de la automatización de Microsoft Office no tienen un precio ni una licencia para soluciones del lado del servidor ([Licenciamiento de los Componentes Web de Office 2000 y las Extensiones del Servidor de Office](#)); por lo tanto, no hay una solución de licenciamiento adecuada para implementar aplicaciones web que utilicen los componentes de Microsoft Office. Aspose ofrece una solución muy económica para aplicaciones basadas en el servidor también.

### **Características**

Los componentes de Aspose proporcionan todo lo necesario para manejar archivos de Office, y mucho más. Están diseñados con la filosofía de permitir a los desarrolladores lograr los mejores resultados con la menor cantidad de trabajo. A diferencia de la automatización de Office, los componentes de Aspose proporcionan muchas funciones poderosas que ahorran tiempo. Por ejemplo, [Aspose.Cells](https://products.aspose.com/cells/) ofrece a los desarrolladores la capacidad de exportar desde un **DataTable** o **DataView** directamente a un archivo de Excel. [Aspose.Words](https://products.aspose.com/words/) ofrece una característica similar que permite a los desarrolladores rellenar un documento de combinación de correspondencia de Word directamente desde cualquier objeto de datos .NET. [Cada componente](https://products.aspose.com/total/) en la familia de Aspose ofrece su propio conjunto de características únicas y poderosas.

La mejor parte de comprar un componente de Aspose o un conjunto de componentes es tener acceso a nuestros equipos de desarrollo. Nuestros equipos de desarrollo se dan cuenta de que si hay una característica que su empresa necesita, muy probablemente otras empresas también la necesitarán. Si bien no todas las solicitudes de características pueden ser agregadas, nuestros equipos intentan ser muy abiertos y flexibles al brindar asistencia. Esa mentalidad es lo que ha ayudado a los componentes de Aspose a convertirse en tan poderosos como son. Si hay características adicionales que necesita de los objetos de automatización de Office, sus posibilidades de tenerlas agregadas son muy, muy bajas.

## **Conclusión**

{{% alert color="primary" %}}

Este artículo ha cubierto los puntos clave sobre por qué los componentes de Aspose son una mejor elección que la automatización de Office. Todos los diferentes componentes de Aspose ofrecen una versión de evaluación sin riesgos ni obligaciones [aquí](https://downloads.aspose.com/total). Le animamos a aprovechar esa evaluación para ver mejor qué puede hacer Aspose por sus aplicaciones.


{{% /alert %}}
