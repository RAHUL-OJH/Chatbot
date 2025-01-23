css = '''

<style>
body {
    background-color: #000000; /* Set background color to black */
    color: #ffffff; /* Set default text color to white for better contrast */
    font-family: "Arial", sans-serif;
}

.chat-message {
    padding: 1rem; 
    border-radius: 0.8rem; 
    margin-bottom: 1rem; 
    display: flex; 
    align-items: flex-start; 
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
}
.chat-message.user {
    background-color: #ffedd5; 
    border: 1px solid #fb923c; 
    color: #000000;
}
.chat-message.bot {
    background-color: #dbeafe; 
    border: 1px solid #3b82f6; 
    color: #000000;
}
.chat-message .avatar {
    width: 50px; 
    height: 50px; 
    border-radius: 50%; 
    overflow: hidden;
    margin-right: 1rem;
}
.chat-message .avatar img {
    width: 100%; 
    height: 100%; 
    object-fit: cover;
}
.chat-message .message {
    flex: 1; 
    font-size: 16px; 
    line-height: 1.6; 
    font-family: "Arial", sans-serif;
    word-wrap: break-word;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://t3.ftcdn.net/jpg/02/15/61/92/360_F_215619203_9mmrDaPnSHOUBfz9XVkjBAknw5XFEK0D.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn.pixabay.com/photo/2021/07/02/04/48/user-6380868_640.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
