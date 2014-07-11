var WPAPP = {};

WPAPP.Models = {};
WPAPP.Collections = {};
WPAPP.Views = {};
WPAPP.Routers = {};


/* = MODELS ======================================== */

WPAPP.Models.Chapter = Backbone.Model.extend();

WPAPP.Models.Article = Backbone.Model.extend();


/* = COLLECTIONS ================================== */

WPAPP.Collections.Chapters = Backbone.Collection.extend({
    model: WPAPP.Models.Chapter
});

WPAPP.Collections.chapters = new WPAPP.Collections.Chapters();

WPAPP.Collections.Articles = Backbone.Collection.extend({
    model: WPAPP.Models.Article
});

WPAPP.Collections.articles = new WPAPP.Collections.Articles();


/* = VIEWS ======================================== */


WPAPP.Views.ItemView = Backbone.View.extend({

    el: '.main-region',

    template: _.template($('#items-template').html()),
    template_chapter: _.template($('#chapter-template').html()),

    initialize: function() {
        console.log("[ ItemView has been initialized ]");

        this.$items = this.$el.find(".items-js");
        this.$title_item = this.$el.find(".title-item-js");
        this.$content_item = this.$el.find(".content-item-js");

        this.render();
    },

    events: {
        "click .item-js": "openItem",
    },

    openItem: function(e) {
        e.preventDefault();
        var item_slug = $(e.currentTarget).data("slug");
        var item_kind = $(e.currentTarget).data("kind");
        var item_selected = this.searchItem(item_slug, item_kind);

        this.$title_item.html(item_selected.title);

        this.$content_item.html(this.template_chapter({
            dato: item_selected
        }));
    },

    searchItem: function(slug, kind) {
        if (kind == 'chapter') {
            var itemsel = _.find(window.datos.chapters, function(item) {
                return item.slug == slug;
            });
        } else {
            var itemsel = _.find(window.datos.articles, function(item) {
                return item.slug == slug;
            });
        }
        return itemsel;
    },

    render: function() {
        this.$items.html("");
        this.$items.append(this.template({
            datos: this.collection
        }));
        return this;
    },
});

WPAPP.Views.AppView = Backbone.View.extend({

    el: '.menu-js',

    initialize: function(config) {
        console.log("[ AppView has been initialized ]");
    },

    events: {
        "click .chapters-link-js": "renderChapters",
        "click .articles-link-js": "renderArticles",
    },

    renderChapters: function(e) {
        e.preventDefault();
        var itemView = new WPAPP.Views.ItemView({
            collection: window.datos.chapters
        });

        this.clearContent(itemView);
    },

    renderArticles: function(e) {
        e.preventDefault();
        var itemView = new WPAPP.Views.ItemView({
            collection: window.datos.articles
        });

        this.clearContent(itemView);
    },

    clearContent: function(itemView) {
        itemView.$title_item.html("Title of chapter/article");
        itemView.$content_item.html("<p>Click en Chapter or Articles menu.</p>");
    }
});

$(function() {

    WPAPP.Views.appView = new WPAPP.Views.AppView();

});