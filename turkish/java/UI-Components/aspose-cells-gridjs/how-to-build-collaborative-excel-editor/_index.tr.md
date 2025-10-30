---
title: GridJs ile işbirlikli Excel düzenleyici nasıl kurulur
type: docs
weight: 260
url: /tr/java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor/
keywords: GridJs,işbirliği,excel düzenleyici,tablo,java
description: Bu makale, Aspose.Cells.GridJs kullanarak Java için işbirlikli bir Excel düzenleyici nasıl oluşturulacağını tanıtmaktadır.
aliases:
  - /java/aspose-cells-gridjs/collaborative-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-spreadsheet-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor-using-gridjs/
---

# İşbirlikli Excel Düzenleyici Rehberi

## Mimari Genel Bakış

Aşağıdaki diyagram, GridJs'in çoklu kullanıcı ile işbirlikli düzenlemeyi nasıl mümkün kıldığını gösteriyor, 
bir Spring Boot arka uç, WebSocket iletişimi ve durum yönetimi için bir MySQL veritabanı ile.

![GridJs İşbirlikli Mimari](gridjs_collaborative_architecture.png)

## Önkoşullar

Başlamadan önce, aşağıdakilerin yüklü olduğundan emin olun:

- **Java 8+**  
- **Maven**  
- **MySQL** (veya desteklenen başka bir SQL veritabanı)  
- (İsteğe bağlı) **Docker** eğer kapsayıcılar içinde çalışmayı tercih ediyorsanız  
- Geçerli bir **Aspose.Cells lisansı** (veya [geçici lisans](https://purchase.aspose.com/temporary-license))  

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

Bu, çoklu kullanıcıların aynı tabloyu aynı anda düzenlemesine olanak tanır.  
Değişiklikler veritabanında saklanır ve gerçek zamanlı olarak istemciler arasında senkronize edilir.

---

## Step 3: Run the Application

Run with Maven:

```bash
mvn spring-boot:run
```

Ana sınıftan doğrudan:

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

## Adım 5: Docker'da Çalıştır (İsteğe bağlı)

Docker kullanıyorsanız, lisans dosyasını eşlemek için [`docker-compose.yml`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/docker-compose.yml) dosyasının 10. satırını düzenleyin.  

Örneğin, lisans dosyanız `C:/license/aspose.lic` ise:

```yaml
volumes:
  - C:/license/aspose.lic:/app/license  # optional: set Aspose license file
```

Bu, yerel dosyayı konteynıra eşler.

Sonra derleyin ve çalıştırın:

```bash
docker-compose up --build
```

Ulaşmak için uygulamaya:  
👉 `http://localhost:8080/gridjsdemo/list`

---

## Key Configuration Details

### 1. Enable Collaborative Mode

In [`/src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties):

```properties
gridjs.iscollabrative=true
```

Sunucu tarafı yapılandırmasında [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

```java
@Bean
public GridJsOptions gridJsOptions() {
    //..... other options
    //here we shall set true for collaborative mode
    options.setCollaborative(true);
    return options;
}
```

Veya küresel olarak:

```java
Config.setCollaborative(true);
```

İstemci tarafı yükleme seçeneklerinde [`/src/main/resources/templates/file/index.html`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/templates/file/index.html):

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


[`/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java):

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

GridJs, `messageTopic`'in varsayılan olarak `/topic/opr` ile eşleşmesini bekler:

```java
com.aspose.gridjs.Config.setMessageTopic("/topic/opr");
```

Veya:

```java
@Bean
    public GridJsOptions gridJsOptions() {
	//.... other options
    	options.setMessageTopic("/topic/opr");
    	//.... other options
        return options;
    }
```

İstemci tarafında:

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws','/app/opr','/user/queue','/topic/opr');
```

Burada, `/GridJs2/msg`, tanımlı yönlendirme yolu ile karşılık gelir  
[`src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java):

```java
@RequestMapping("/GridJs2/msg")
```

#### Özel WebSocket yolları ile örnek

Sunucunuz farklı bir yapılandırma kullanıyorsa:

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

O zaman aşağıdaki ayarları yapmalısınız:

**Sunucu tarafı**:

```java
com.aspose.gridjs.Config.setMessageTopic("/topic_gridjs/opr");
```

veya

```java
    @Bean
    public GridJsOptions gridJsOptions() {
	//.... other option
    	options.setMessageTopic("/topic_gridjs/opr");
    	//.... other option
        return options;
    }
```

**İstemci tarafı**:

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws_gridjs','/app_gridjs/opr','/user_gridjs/queue','/topic_gridjs/opr');
```

setCollaborativeSetting için detaylı dokümantasyonu [burada](https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/) bulabilirsiniz

> ⚠️ Not: Varsayılan olarak, demo yapılandırması anında çalışır.  
Ek yapılandırma yalnızca uygulamanız WebSocket uç noktalarını özelleştiriyorsa gerekir.  

Ayrıca unutmayın: işbirlikçi mod **tembel yükleme** desteği sağlamaz.  
`Config.setLazyLoading(true)` etkinleştirmeyin.

---

## Additional Notes


- We can add **file uploads** to load and edit spreadsheet file from upload directory.  
- Integrate with **cloud storage** like AWS S3 or Azure Blob.  

---

## Sonuç

Aspose.Cells.GridJs ile güçlü bir **işbirlikçi Excel düzenleyici** hızlıca oluşturabilirsiniz.  
Java backend, GridJs frontend, SQL depolama ve WebSocket mesajlaşmasının kombinasyonu güvenilir gerçek zamanlı elektronik tablo düzenlemesini sağlar.

---

## Resources

- [Product Page](https://products.aspose.com/cells/java)  
- [Documentation](https://docs.aspose.com/cells/java/aspose-cells-gridjs/)  
- [API Reference](https://reference.aspose.com/cells/java/com.aspose.gridjs/)  
- [Support Forum](https://forum.aspose.com/c/cells)  
- [Free Online Apps](https://products.aspose.app/cells/family)  
