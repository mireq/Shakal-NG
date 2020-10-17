# -*- coding: utf-8 -*-
from __future__ import unicode_literals

SPRITES = (
	{
		'name': 'sprites',
		'output': 'alpha/images/sprites.png',
		'scss_output': 'alpha/scss/_sprites.scss',
		'extra_sizes': ((2, '@2x'),),
		'width': 400,
		'height': 400,
		'images': (
			{ 'name': 'header_shadow', 'src': 'alpha/images/header_shadow.png', 'mode': 'repeat-x' },
			{ 'name': 'logo', 'src': 'alpha/images/png/logo.png', },
			{ 'name': 'logo_mini', 'src': 'alpha/images/png/logo_mini.png', },
			{ 'name': 'avatar_placeholder', 'src': 'alpha/images/png/avatar_placeholder.png', },
			{ 'name': 'user_dark', 'src': 'alpha/images/png/user_dark.png' },
			{ 'name': 'user_light', 'src': 'alpha/images/png/user_light.png' },
			{ 'name': 'user_rating_0_dark', 'src': 'alpha/images/png/rating_0_transparent_dark.png' },
			{ 'name': 'user_rating_0_light', 'src': 'alpha/images/png/rating_0_transparent_light.png' },
			{ 'name': 'user_rating_1_dark', 'src': 'alpha/images/png/rating_1_transparent_dark.png' },
			{ 'name': 'user_rating_1_light', 'src': 'alpha/images/png/rating_1_transparent_light.png' },
			{ 'name': 'user_rating_2_dark', 'src': 'alpha/images/png/rating_2_transparent_dark.png' },
			{ 'name': 'user_rating_2_light', 'src': 'alpha/images/png/rating_2_transparent_light.png' },
			{ 'name': 'user_rating_3_dark', 'src': 'alpha/images/png/rating_3_transparent_dark.png' },
			{ 'name': 'user_rating_3_light', 'src': 'alpha/images/png/rating_3_transparent_light.png' },
			{ 'name': 'user_rating_4_dark', 'src': 'alpha/images/png/rating_4_transparent_dark.png' },
			{ 'name': 'user_rating_4_light', 'src': 'alpha/images/png/rating_4_transparent_light.png' },
			{ 'name': 'user_rating_5_dark', 'src': 'alpha/images/png/rating_5_transparent_dark.png' },
			{ 'name': 'user_rating_5_light', 'src': 'alpha/images/png/rating_5_transparent_light.png' },
			{ 'name': 'user_rating_admin_dark', 'src': 'alpha/images/png/rating_admin_transparent_dark.png' },
			{ 'name': 'user_rating_admin_light', 'src': 'alpha/images/png/rating_admin_transparent_light.png' },
			{ 'name': 'facebook', 'src': 'images/facebook.png' },
			{ 'name': 'twitter', 'src': 'images/twitter.png' },
			{ 'name': 'vybralisme', 'src': 'images/vybralisme.png' },
			{ 'name': 'menu_dark', 'src': 'alpha/images/png/menu_dark.png' },
			{ 'name': 'menu_light', 'src': 'alpha/images/png/menu_light.png' },
			{ 'name': 'menu_back_dark', 'src': 'alpha/images/png/menu_back_dark.png' },
			{ 'name': 'menu_back_light', 'src': 'alpha/images/png/menu_back_light.png' },
			{ 'name': 'block_dark', 'src': 'alpha/images/png/block_transparent_dark.png' },
			{ 'name': 'block_light', 'src': 'alpha/images/png/block_transparent_light.png' },
			{ 'name': 'comments_dark', 'src': 'alpha/images/png/comments_transparent_dark.png' },
			{ 'name': 'comments_light', 'src': 'alpha/images/png/comments_transparent_light.png' },
			{ 'name': 'delete_red', 'src': 'alpha/images/png/delete_red.png' },
			{ 'name': 'eye_dark', 'src': 'alpha/images/png/eye_transparent_dark.png' },
			{ 'name': 'eye_light', 'src': 'alpha/images/png/eye_transparent_light.png' },
			{ 'name': 'eye_blue', 'src': 'alpha/images/png/eye_blue.png' },
			{ 'name': 'flag_dark', 'src': 'alpha/images/png/flag_transparent_dark.png' },
			{ 'name': 'flag_light', 'src': 'alpha/images/png/flag_transparent_light.png' },
			{ 'name': 'gear_dark', 'src': 'alpha/images/png/gear_dark.png' },
			{ 'name': 'gear_light', 'src': 'alpha/images/png/gear_light.png' },
			{ 'name': 'lock_dark', 'src': 'alpha/images/png/lock_transparent_dark.png' },
			{ 'name': 'lock_light', 'src': 'alpha/images/png/lock_transparent_light.png' },
			{ 'name': 'unlock_dark', 'src': 'alpha/images/png/unlock_transparent_dark.png' },
			{ 'name': 'unlock_light', 'src': 'alpha/images/png/unlock_transparent_light.png' },
			{ 'name': 'pencil_dark', 'src': 'alpha/images/png/pencil_transparent_dark.png' },
			{ 'name': 'pencil_light', 'src': 'alpha/images/png/pencil_transparent_light.png' },
			{ 'name': 'parent_dark', 'src': 'alpha/images/png/parent_transparent_dark.png' },
			{ 'name': 'parent_light', 'src': 'alpha/images/png/parent_transparent_light.png' },
			{ 'name': 'reply_dark', 'src': 'alpha/images/png/reply_transparent_dark.png' },
			{ 'name': 'reply_light', 'src': 'alpha/images/png/reply_transparent_light.png' },
			{ 'name': 'rss_dark', 'src': 'alpha/images/png/rss_dark.png' },
			{ 'name': 'rss_light', 'src': 'alpha/images/png/rss_light.png' },
			{ 'name': 'search_dark', 'src': 'alpha/images/png/search_dark.png' },
			{ 'name': 'search_light', 'src': 'alpha/images/png/search_light.png' },
			{ 'name': 'search_transparent_dark', 'src': 'alpha/images/png/search_transparent_dark.png' },
			{ 'name': 'search_transparent_light', 'src': 'alpha/images/png/search_transparent_light.png' },
			{ 'name': 'star_yellow', 'src': 'alpha/images/png/star_yellow.png' },
			{ 'name': 'tick_green', 'src': 'alpha/images/png/tick_green.png' },
			{ 'name': 'arrow_down_dark', 'src': 'alpha/images/png/arrow_down_dark.png' },
			{ 'name': 'arrow_down_light', 'src': 'alpha/images/png/arrow_down_light.png' },
			{ 'name': 'foldable_closed_transparent_dark', 'src': 'alpha/images/png/foldable_closed_transparent_dark.png' },
			{ 'name': 'foldable_closed_transparent_light', 'src': 'alpha/images/png/foldable_closed_transparent_light.png' },
			{ 'name': 'foldable_open_transparent_dark', 'src': 'alpha/images/png/foldable_open_transparent_dark.png' },
			{ 'name': 'foldable_open_transparent_light', 'src': 'alpha/images/png/foldable_open_transparent_light.png' },
			{ 'name': 'trashcan_transparent_dark', 'src': 'alpha/images/png/trashcan_transparent_dark.png' },
			{ 'name': 'trashcan_transparent_light', 'src': 'alpha/images/png/trashcan_transparent_light.png' },
		),
	},
	{
		'name': 'sprites',
		'output': '2013/images/backgrounds.png',
		'scss_output': '2013/_sprites.scss',
		'extra_sizes': (),
		'width': 1200,
		'height': 1200,
		'images': (
			{ 'name': 'btn_std', 'src': '2013/images/btn_std.png' },
			{ 'name': 'btn_std_hover', 'src': '2013/images/btn_std_hover.png' },
			{ 'name': 'btn_act', 'src': '2013/images/btn_act.png' },
			{ 'name': 'btn_act_hover', 'src': '2013/images/btn_act_hover.png' },
			{ 'name': 'btn_content_std', 'src': '2013/images/btn_content_std.png' },
			{ 'name': 'btn_content_std_hover', 'src': '2013/images/btn_content_std_hover.png' },
			{ 'name': 'btn_content_act', 'src': '2013/images/btn_content_act.png' },
			{ 'name': 'btn_content_act_hover', 'src': '2013/images/btn_content_act_hover.png' },
			{ 'name': 'breadcrumb_panel_bg', 'src': '2013/images/breadcrumb_panel_bg.png', 'mode': 'repeat-x' },
			{ 'name': 'breadcrumb_std', 'src': '2013/images/breadcrumb.png' },
			{ 'name': 'breadcrumb_act', 'src': '2013/images/breadcrumb_act.png' },
			{ 'name': 'tabs_std', 'src': '2013/images/tabs_std.png' },
			{ 'name': 'tabs_act', 'src': '2013/images/tabs_act.png' },
			{ 'name': 'logo', 'src': '2013/images/logo.png' },
			{ 'name': 'avatar_placeholder', 'src': '2013/images/avatar_placeholder.png' },
			{ 'name': 'user_rating_0', 'src': '2013/images/rating_0.png' },
			{ 'name': 'user_rating_1', 'src': '2013/images/rating_1.png' },
			{ 'name': 'user_rating_2', 'src': '2013/images/rating_2.png' },
			{ 'name': 'user_rating_3', 'src': '2013/images/rating_3.png' },
			{ 'name': 'user_rating_4', 'src': '2013/images/rating_4.png' },
			{ 'name': 'user_rating_5', 'src': '2013/images/rating_5.png' },
			{ 'name': 'user_rating_admin', 'src': '2013/images/rating_admin.png' },
			{ 'name': 'facebook', 'src': 'images/facebook.png' },
			{ 'name': 'twitter', 'src': 'images/twitter.png' },
			{ 'name': 'vybralisme', 'src': 'images/vybralisme.png' },
			{ 'name': 'breadcrumb_bg', 'src': '2013/images/breadcrumb_bg.png' },
			{ 'name': 'breadcrumb_bg_reverse', 'src': '2013/images/breadcrumb_bg_reverse.png' },
			{ 'name': 'breadcrumb_home', 'src': '2013/images/breadcrumb_home.png' },
			{ 'name': 'dropdown_icon_14', 'src': '2013/images/dropdown_icon_14.png' },
			{ 'name': 'profile_icon_14', 'src': '2013/images/profile_icon_14.png' },
			{ 'name': 'search_icon', 'src': '2013/images/search_icon.png' },
			{ 'name': 'rss_icon', 'src': '2013/images/rss_icon.png' },
			{ 'name': 'settings_icon', 'src': '2013/images/settings_icon.png' },
			{ 'name': 'trashcan', 'src': '2013/images/trashcan.png' },
			{ 'name': 'corner_arrow_up', 'src': '2013/images/corner_arrow_up.png' },
			{ 'name': 'locked_icon', 'src': '2013/images/locked.png' },
			{ 'name': 'new_icon', 'src': '2013/images/new.png' },
			{ 'name': 'tick_icon', 'src': '2013/images/tick.png' },
			{ 'name': 'watch_icon', 'src': '2013/images/watch.png' },
			{ 'name': 'comment_icon_14', 'src': '2013/images/comment_icon_14.png' },
			{ 'name': 'watch_icon_14', 'src': '2013/images/watch_icon_14.png' },
			{ 'name': 'tick_icon_14', 'src': '2013/images/tick_icon_14.png' },
			{ 'name': 'lock_icon_14', 'src': '2013/images/lock_icon_14.png' },
			{ 'name': 'up_icon_14', 'src': '2013/images/up_icon_14.png' },
			{ 'name': 'down_icon_14', 'src': '2013/images/down_icon_14.png' },
			{ 'name': 'delete_icon_14', 'src': '2013/images/delete_icon_14.png' },
			{ 'name': 'settings_icon_14', 'src': '2013/images/settings_icon_14.png' },
			{ 'name': 'header_bg', 'src': '2013/images/header_bg.png', 'mode': 'repeat-x' },
			{ 'name': 'block_header_bg', 'src': '2013/images/block_header_bg.png', 'mode': 'repeat-x' },
			{ 'name': 'submit_row_bg', 'src': '2013/images/submit_row_bg.png', 'mode': 'repeat-x' },
			{ 'name': 'input_bg', 'src': '2013/images/input_bg.png', 'mode': 'repeat-x' },
			{ 'name': 'progress', 'src': '2013/images/progressbar.png', 'mode': 'repeat-x' },
			{ 'name': 'progress_bar', 'src': '2013/images/progressbar_bar.png', 'mode': 'repeat-x' },
		),
	},
)

ASSETS = {
	'utils': {
		'js': 'static://django_ajax_utils/js/utils.js',
	},
	'utils_ajax': {
		'js': 'static://django_ajax_utils/js/utils_ajax.js',
		'depends': ['utils'],
	},
	"utils2": {
		"js": "static://js/utils.js",
	},
	"menu": {
		"js": "static://js/menu.js",
		'depends': ['utils_ajax'],
	},
	"menu2": {
		"js": "static://js/menu2.js",
		'depends': ['utils2'],
	},
	"messages": {
		"js": "static://js/messages.js",
		'depends': ['utils_ajax'],
	},
	"messages2": {
		"js": "static://js/messages2.js",
		'depends': ['utils2'],
	},
	"toggle": {
		"js": "static://js/toggle.js",
		'depends': ['utils_ajax'],
	},
	"modal": {
		"js": "static://js/modal.js",
		'depends': ['utils2', 'utils_ajax'],
	},
	"comments": {
		"js": "static://js/comments.js",
		'depends': ['modal', 'utils2'],
	},
}
