---
title: كيفية بناء محرر Excel تعاوني باستخدام GridJs
type: docs
weight: 260
url: /ar/java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor/
keywords: GridJs،تعاوني،محرر إكسل،جدول بيانات،Java
description: يقدم هذا المقال شرحًا لكيفية بناء محرر إكسل تعاوني باستخدام Aspose.Cells.GridJs لـ Java.
aliases:
  - /java/aspose-cells-gridjs/collaborative-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-spreadsheet-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor-using-gridjs/
---

# دليل المحرر التعاوني لإكسل

## نظرة عامة على الهندسة المعمارية

يوضح الرسم التالي كيف يمكّن GridJs من التحرير التعاوني بمشاركة عدة مستخدمين، 
خلفية Spring Boot، اتصال عبر WebSocket، و قاعدة بيانات MySQL لإدارة الحالة.

![هيكلية التعاونية لـ GridJs](gridjs_collaborative_architecture.png)

## متطلبات قبلية

قبل البدء، تأكد من أن لديك الملفات التالية مثبتة:

- **Java 8+**  
- **Maven**  
- **MySQL** (أو قاعدة بيانات SQL مدعومة أخرى)  
- (اختياري) **Docker** إذا فضلت التشغيل في حاويات  
- ترخيص **Aspose.Cells** صالح (أو [ترخيص مؤقت](https://purchase.aspose.com/temporary-license))  

---

## Step 1: Clone the Demo Project

Clone the official [Aspose.Cells GridJs demo repository](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs.Collaborative):

```bash
git clone https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java.git
cd Aspose.Cells-for-Java/Examples.GridJs.Collaborative
```

---

## Step 2: Configure Collaborative Mode

Open the [`src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties) file and adjust the settings:

```properties
# Directory containing spreadsheet files
testconfig.ListDir=/app/wb

# Directory for storing cache files
testconfig.CachePath=/app/grid_cache

# Aspose.Cells license file
testconfig.AsposeLicensePath=/app/license

# Enable collaborative mode
gridjs.iscollabrative=true

# Database connection (example: MySQL)
spring.datasource.url=jdbc:mysql://localhost:3306/gridjsdemodb?createDatabaseIfNotExist=true&useUnicode=true&serverTimezone=UTC&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
spring.sql.init.platform=mysql
```

هذا يسمح لمستخدمين متعددين بتحرير نفس جدول البيانات في الوقت ذاته.  
يتم تخزين التغييرات في قاعدة البيانات ومزامنتها بين العملاء في الوقت الحقيقي.

---

## Step 3: Run the Application

Run with Maven:

```bash
mvn spring-boot:run
```

أو مباشرة من الفئة الرئيسية:

```
src/main/java/com/aspose/gridjsdemo/usermanagement/UserManagementApplication.java
```

---

## Step 4: Test Collaborative Editing

Open your browser and navigate to:  
👉 `http://localhost:8080/gridjsdemo/list`

Steps:

1. A login page appears. Click **Create User** to register User1 and log in. You will then see the file list.  
2. Open a file from the list. The spreadsheet editor will load.  
3. Copy the same URL into another browser window. It will redirect to the login page. Create User2 and log in.  
4. Both users now see the same spreadsheet.  
5. If User1 edits the spreadsheet, User2 will see the changes in real time.  
6. If User2 edits, User1 will see the changes as well.  
7. Users can also download and save the file.  

---

## الخطوة 5: التشغيل في دوكر (اختياري)

إذا كنت تعمل في دوكر، قم بتحرير السطر 10 من [`docker-compose.yml`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/docker-compose.yml) لتهيئة ملف الترخيص.  

على سبيل المثال، إذا كان ملف الترخيص الخاص بك في `C:/license/aspose.lic`:

```yaml
volumes:
  - C:/license/aspose.lic:/app/license  # optional: set Aspose license file
```

يقوم هذا بربط الملف المحلي داخل الحاوية.

ثم بناء وتشغيل:

```bash
docker-compose up --build
```

الوصول إلى التطبيق عبر:  
👉 `http://localhost:8080/gridjsdemo/list`

---

## Key Configuration Details

### 1. Enable Collaborative Mode

In [`/src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties):

```properties
gridjs.iscollabrative=true
```

في إعدادات الخادم [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

```java
@Bean
public GridJsOptions gridJsOptions() {
    //..... other options
    //here we shall set true for collaborative mode
    options.setCollaborative(true);
    return options;
}
```

أو بشكل عام:

```java
Config.setCollaborative(true);
```

في خيارات تحميل العميل [`/src/main/resources/templates/file/index.html`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/templates/file/index.html):

```js
const option = {
    //..... other options
    //here we shall set true for collaborative mode
    isCollaborative: true
    //..... other options
};
```

---

### 2. User System Integration

The demo uses **Spring Security** for a simple user system.  

You must provide a `CoWorkUserProvider` implementation to connect GridJs with your user system:

In server-side config [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

For example: here we defined MyCustomUser to implement all the interfaces in CoWorkUserProvider.

```java
@Bean
public CoWorkUserProvider currentUserProvider() {
    return new MyCustomUser();
}
```


في [`/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java):

```java
public class MyCustomUser implements CoWorkUserProvider {
    //Get the current login user name
    @Override
    public String getCurrentUserName() {
        return getCurrentUser().getUsername();
    }

    //Get the current login user Id
    @Override
    public Long getCurrentUserId() {
        return getCurrentUser().getUserId();
    }

    //Get the current login user permission
    @Override
    public CoWorkUserPermission getPermission() {
        return CoWorkUserPermission.EDITABLE;
    }

    private static CustomUserDetails getCurrentUser() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication != null && authentication.getPrincipal() instanceof CustomUserDetails) {
            return (CustomUserDetails) authentication.getPrincipal();
        }
        throw new IllegalStateException("User not authenticated");
    }
}
```

---

### 3. WebSocket Configuration

The demo uses **Spring WebSocket** with STOMP.  

Example config:

In [`/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java):

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic");
        config.setApplicationDestinationPrefixes("/app");
        config.setUserDestinationPrefix("/user");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

يتوقع GridJs أن يطابق `messageTopic` مع "/topic/opr" وهو الافتراضي:

```java
com.aspose.gridjs.Config.setMessageTopic("/topic/opr");
```

أو:

```java
@Bean
    public GridJsOptions gridJsOptions() {
	//.... other options
    	options.setMessageTopic("/topic/opr");
    	//.... other options
        return options;
    }
```

على جانب العميل:

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws','/app/opr','/user/queue','/topic/opr');
```

هنا، `/GridJs2/msg` يتوافق مع مسار الطريق المحدد في  
[`src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java):

```java
@RequestMapping("/GridJs2/msg")
```

#### مثال مع مسارات ويب سوكيت مخصصة

إذا كان سيرفرك يستخدم إعدادات مختلفة:

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic_gridjs");
        config.setApplicationDestinationPrefixes("/app_gridjs");
        config.setUserDestinationPrefix("/user_gridjs");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws_gridjs")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

ثم يجب عليك تعيين:

**جانب الخادم**:

```java
com.aspose.gridjs.Config.setMessageTopic("/topic_gridjs/opr");
```

أو

```java
    @Bean
    public GridJsOptions gridJsOptions() {
	//.... other option
    	options.setMessageTopic("/topic_gridjs/opr");
    	//.... other option
        return options;
    }
```

**جانب العميل**:

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws_gridjs','/app_gridjs/opr','/user_gridjs/queue','/topic_gridjs/opr');
```

يمكن العثور على وثيقة التفاصيل لإعدادCollaborativeSetting [هنا](https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/)

> ⚠️ ملاحظة: بشكل افتراضي، يعمل تكوين العرض التوضيحي مباشرة بدون تعديلات.  
يُطلب تكوين إضافي فقط إذا كانت تطبيقك تخصص نقاط نهاية WebSocket.  

وتذكّر أيضًا: وضع التعاون **لا** يدعم التحميل الكسول.  
لا تفعّل `Config.setLazyLoading(true)`.

---

## Additional Notes


- We can add **file uploads** to load and edit spreadsheet file from upload directory.  
- Integrate with **cloud storage** like AWS S3 or Azure Blob.  

---

## الخاتمة

مع Aspose.Cells.GridJs، يمكنك بسرعة بناء **محرر Excel التعاوني** قوي.  
يكفل دمج خلفية جافا، واجهة GridJs، تخزين SQL، ورسائل WebSocket تحرير جداول بيانات موثوق في الوقت الحقيقي.

---

## Resources

- [Product Page](https://products.aspose.com/cells/java)  
- [Documentation](https://docs.aspose.com/cells/java/aspose-cells-gridjs/)  
- [API Reference](https://reference.aspose.com/cells/java/com.aspose.gridjs/)  
- [Support Forum](https://forum.aspose.com/c/cells)  
- [Free Online Apps](https://products.aspose.app/cells/family)  
