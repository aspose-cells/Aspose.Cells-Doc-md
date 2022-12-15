---
title: Instalar Aspose.Cells en Windows
type: docs
weight: 20
url: /es/net/installing-aspose-cells-on-windows/
---
{{% alert color="primary" %}} 

 A veces puede enfrentar algunos problemas al instalar**Aspose.Cells** usando su paquete de instalación (Aspose.Cells.msi...Windows Paquete de instalación) en**Windows Vista** . Este documento explica cómo podemos hacerle frente e implementar la instalación exitosa del componente. Realmente**Aspose.Cells**El instalador necesita crear una carpeta virtual en IIS para la implementación de sus demostraciones web (Asp.NET Demos) en su máquina, por lo que debe tener privilegios de administración antes de instalar**Aspose.Cells** utilizando su instalador. El instalador exige que se le permita explícitamente el acceso de nivel de administrador al sistema.

{{% /alert %}} 
## **Posibles factores**
 Normalmente, en**Windows Vista** , los productos/componentes que instala/utiliza siempre se implementan con permisos de "usuario normal", incluso si es un**Administrador** . Los programas solo tienen acceso limitado al sistema de archivos, incluso si ha iniciado sesión como usuario.**Administrador** . Esto tiene algunos efectos secundarios desafortunados que normalmente no encontrarías en Windows XP cuando inicias sesión como usuario.**Administrador**.
## **UAC (Control de cuentas de usuario)**
**UAC** es la parte de**Windows Vista** que te pide permiso. los**UAC** Modo (también conocido como**Modo de aprobación del administrador** ) es un modo de operación que (principalmente) afecta la forma en que funcionan las cuentas de administrador. Cuando**UAC**está activado (lo que está predeterminado), debe otorgar permiso explícitamente a cualquier programa que quiera usar los poderes de "administrador". Se negará el acceso a cualquier programa que intente usar los poderes de administrador sin su permiso.**UAC** también se requiere para otras características de seguridad de**Windows Vista** , incluido**Modo protegido** en Internet Explorer. El modo protegido de Internet Explorer protege su computadora de páginas web no autorizadas y otras vulnerabilidades relacionadas con la web, incluidas las desconocidas.

 Cuando**UAC** está habilitado, cada programa que ejecute tendrá acceso al sistema únicamente como "usuario estándar", incluso cuando haya iniciado sesión como administrador.**Windows Vista** tiene la capacidad incorporada de reducir automáticamente el potencial de brechas de seguridad en el sistema. Lo hace habilitando automáticamente esta característica llamada**Control de cuentas del usuario** (o**UAC** para abreviar). los**UAC**obliga a los usuarios que forman parte del grupo de administradores locales a ejecutarse como si fueran usuarios normales sin privilegios administrativos. A pesar de que**UAC** mejora claramente la seguridad en**Windows Vista** , en algunos escenarios es posible que desee deshabilitarlo, por ejemplo, al realizar demostraciones frente a una audiencia (demostraciones que no están relacionadas con la seguridad, por ejemplo). Algunos usuarios domésticos pueden tener la tentación de desactivar**UAC** debido al uso de recursos adicionales de su sistema.
## **Pasos necesarios para la instalación exitosa del componente**
-  Asegúrese de que IIS esté instalado en su Vista antes de instalar**Aspose.Cells** . Es obligatorio porque**Aspose.Cells** El instalador necesita crear una carpeta virtual en IIS para la implementación de Web Demos (Asp.NET Demos).
-  Necesitas deshabilitar**UAC** (Control de cuentas del usuario). Tienes que asegurarte de tener un**Privilegios de administrador** con control total del sistema antes de instalar**Aspose.Cells** . De lo contrario, podría obtener un error # 2869 durante la instalación**Aspose.Cells**utilizando su instalador.

Las siguientes son algunas maneras de lograr esto.
### **Uso de la línea de comandos**
1.  Busque cmd.exe en su directorio de Windows, luego haga clic derecho sobre él y seleccione Ejecutar como...**Administrador**
 2. Ahora, ejecute el siguiente comando en el símbolo del sistema: msiexec /i<your path>/Aspose.Cells.msi y Enter.
### **Uso del panel de control**
- Haga clic en Inicio
- Haga clic en Panel de control
- Haga clic en Cuentas de usuario y seguridad familiar
- Haga clic en Cuentas de usuario
- Haga clic en Activar o desactivar el Control de cuentas de usuario
- Desmarque la casilla de verificación
- Haga clic en Aceptar

{{% alert color="primary" %}} 

Deberá reiniciar su computadora para que el cambio surta efecto. Este cambio afecta a todas las cuentas de la computadora, no solo a la tuya.

{{% /alert %}}
