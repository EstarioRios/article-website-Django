from django.urls import path
from .views import (
    create_blog,
    sub_comment,
    edit_blog,
    edit_comment,
    remove_blog,
    remove_comment,
    like_comment,
    dislike_comment,
    like_blog,
    dislike_blog,
    deactive_blog,
    active_blog,
)

# ------------------------------
# Document Management API Endpoints
# Base URL prefix: /doc/
# ------------------------------
urlpatterns = [
    # ------------------------------
    # CREATE BLOG
    # Endpoint: POST /doc/create-blog/
    # Description:
    #   - Creates a new blog post.
    #   - Required fields: title, description, content
    #   - Optional field: tags
    #   - Requires JWT authentication
    # ------------------------------
    path("create-blog/", create_blog, name="create_blog"),
    
    # ------------------------------
    # SUBMIT COMMENT
    # Endpoint: POST /doc/sub-comment/
    # Description:
    #   - Adds a comment to a blog post.
    #   - Required fields: content, blog_id
    #   - Requires JWT authentication
    # ------------------------------
    path("sub-comment/", sub_comment, name="sub_comment"),
    
    # ------------------------------
    # EDIT BLOG
    # Endpoint: PUT /doc/edit-blog/
    # Description:
    #   - Updates an existing blog post.
    #   - Required fields: blog_id, new_title, new_description, new_content, new_tags
    #   - User must be the owner of the blog
    #   - Requires JWT authentication
    # ------------------------------
    path("edit-blog/", edit_blog, name="edit_blog"),
    
    # ------------------------------
    # EDIT COMMENT
    # Endpoint: PATCH /doc/edit-comment/
    # Description:
    #   - Updates an existing comment.
    #   - Required fields: commentId, newContent
    #   - User must be the owner of the comment
    #   - Requires JWT authentication
    # ------------------------------
    path("edit-comment/", edit_comment, name="edit_comment"),
    
    # ------------------------------
    # REMOVE BLOG
    # Endpoint: DELETE /doc/remove-blog/
    # Description:
    #   - Deletes a blog post.
    #   - Required field: blog_id
    #   - User must be the owner of the blog
    #   - Requires JWT authentication
    # ------------------------------
    path("remove-blog/", remove_blog, name="remove_blog"),
    
    # ------------------------------
    # REMOVE COMMENT
    # Endpoint: DELETE /doc/remove-comment/
    # Description:
    #   - Deletes a comment.
    #   - Required field: comentId
    #   - User must be the owner of the comment
    #   - Requires JWT authentication
    # ------------------------------
    path("remove-comment/", remove_comment, name="remove_comment"),
    
    # ------------------------------
    # LIKE COMMENT
    # Endpoint: PATCH /doc/like-comment/
    # Description:
    #   - Increments the like count of a comment.
    #   - Required field: comment_id
    #   - Requires JWT authentication
    # ------------------------------
    path("like-comment/", like_comment, name="like_comment"),
    
    # ------------------------------
    # DISLIKE COMMENT
    # Endpoint: PATCH /doc/dislike-comment/
    # Description:
    #   - Increments the dislike count of a comment.
    #   - Required field: comment_id
    #   - Requires JWT authentication
    # ------------------------------
    path("dislike-comment/", dislike_comment, name="dislike_comment"),
    
    # ------------------------------
    # LIKE BLOG
    # Endpoint: PATCH /doc/like-blog/
    # Description:
    #   - Increments the like count of a blog post.
    #   - Required field: blog_id
    #   - Requires JWT authentication
    # ------------------------------
    path("like-blog/", like_blog, name="like_blog"),
    
    # ------------------------------
    # DISLIKE BLOG
    # Endpoint: PATCH /doc/dislike-blog/
    # Description:
    #   - Increments the dislike count of a blog post.
    #   - Required field: blog_id
    #   - Requires JWT authentication
    # ------------------------------
    path("dislike-blog/", dislike_blog, name="dislike_blog"),
    
    # ------------------------------
    # DEACTIVATE BLOG
    # Endpoint: PATCH /doc/deactive-blog/
    # Description:
    #   - Marks a blog post as inactive (not publicly visible).
    #   - Required field: blog_id
    #   - User must be the owner of the blog
    #   - Requires JWT authentication
    # ------------------------------
    path("deactive-blog/", deactive_blog, name="deactive_blog"),
    
    # ------------------------------
    # ACTIVATE BLOG
    # Endpoint: PATCH /doc/active-blog/
    # Description:
    #   - Marks a blog post as active (publicly visible).
    #   - Required field: blog_id
    #   - User must be the owner of the blog
    #   - Requires JWT authentication
    # ------------------------------
    path("active-blog/", active_blog, name="active_blog"),
]