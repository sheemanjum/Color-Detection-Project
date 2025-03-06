<!DOCTYPE html>
<!-- saved from url=(0167)https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4 -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/light-605318cbe3a1.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/dark-bd1cb5575fff.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-52a2075571c3.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-bf3988586de0.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-27a437876a92.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-97f0dc959f8f.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-708e3a93215a.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-9217138a8d5b.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-4397d91bdb49.css">

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/primer-primitives-225433424a87.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/primer-93aded0ee8a1.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/global-21a7f868f707.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/github-15d4b28ab680.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/repository-4fce88777fa8.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/code-0210be90f4d3.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_quote_reply_fix","contentful_lp_optimize_image","contentful_lp_hero_video_cover_image","copilot_immersive_file_preview","copilot_new_references_ui","copilot_chat_repo_custom_instructions_preview","copilot_chat_immersive_subthreading","copilot_chat_retry_on_error","copilot_chat_persist_submitted_input","copilot_conversational_ux_history_refs","copilot_chat_shared_chat_input","copilot_editor_upsells","copilot_implicit_context","copilot_no_floating_button","copilot_smell_icebreaker_ux","copilot_spaces_multi_file_picker","copilot_read_shared_conversation","dotcom_chat_client_side_skills","experimentation_azure_variant_endpoint","failbot_handle_non_errors","geojson_azure_maps","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","github_models_o3_mini_streaming","hovercard_accessibility","insert_before_patch","issues_react_remove_placeholders","issues_react_blur_item_picker_on_close","issues_react_include_bots_in_pickers","marketing_pages_search_explore_provider","remove_child_patch","sample_network_conn_type","swp_enterprise_contact_form","site_copilot_extensions_ga","site_copilot_extensions_hero","site_copilot_vscode_link_update","site_proxima_australia_update","issues_react_create_milestone","issues_react_cache_fix_workaround","lifecycle_label_name_updates"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/wp-runtime-90bd83524e9f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover_js-9da652f58479.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_arianotify-polyfill_ariaNotify-polyfill_js-node_modules_github_mi-3abb8f-d7e6bc799724.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/ui_packages_failbot_failbot_ts-4600dbf2d60a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/environment-f04cb2a9fc8c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_primer_behaviors_dist_esm_index_mjs-0dbb79f97f8f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-f690fd9ae3d5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_relative-time-element_dist_index_js-f6da4b3fa34c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-8e9f78-a74b4e0a8a6b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_text-expander-element_dist_index_js-78748950cb0c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-b5f1d7-a1760ffda83d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_markdown-toolbar-element_dist_index_js-ceef33f593fa.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-c44a69-8094ee2ecc5e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/github-elements-c5fd390b3ba0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/element-registry-a71c0dc18ea2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-bb80ec-72267f4e3ff9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_lit-html_lit-html_js-be8cb88f481b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_morphdom_dist_morphdom-e-7c534c-a4a1922eb55f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-e3cbe28f1638.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-6cf3320416b8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_color-convert_index_js-e3180fe3bcb3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-69cfcc-bc42a18e77d5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/ui_packages_updatable-content_updatable-content_ts-2a55124d5c52.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-900dde-768abe60b1f8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/app_assets_modules_github_sticky-scroll-into-view_ts-3e000c5d31a9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-87a4ae-21948f72ce0b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-e429cff6ceb1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/behaviors-3852665e5a2d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-f6223d90c7ba.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/notifications-global-01e85cd1be94.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-94dc7a2157c1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-70450e-eecf0d50276f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/app_assets_modules_github_ref-selector_ts-3e9d848bab5f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/codespaces-c3bcacfe317c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-3eebbd-0763620ad7bf.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_delegated-events_di-e161aa-9d41fb1b6c9e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_remote--3c9c82-7238cfcdaa51.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/repositories-7a0dbaa42c57.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-26cce2010167.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/code-menu-1c0aedc134b1.js.download"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/primer-react-d4f7d0473d87.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/react-core-56b50d0313a2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/react-lib-f1bca44e0926.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/octicons-react-611691cca2f6.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-62da9f-2df2f32ec596.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-e7dcdd-f7cc96ebae76.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-55fea94174bf.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/notifications-subscriptions-menu-58a0c58bfee4.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/primer-react.694157f711c9f0ff6654.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/notifications-subscriptions-menu.1bcff9205c241e99cff2.module.css">

  



  



  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  




      



        


  <meta http-equiv="x-pjax-version" content="571ac1085a5aaae4beefda66716988e6d95f821f6d93fa56887311523f928ff8" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="1387756d457e2f7c930482f0374bab8f35110d772491ea950a7236d69098c3a6" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="a30977995814647d0827c66025b8a8c5cb8722c27765b03e9e34bf066d054640" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="f4d9a55779d0487ef225f7eab1ab6ba11635106770fbaea31a4666751bc97091" data-turbo-track="reload">

  

      
  

  



      


    


  

  

  
  
  




  
  

  

  <style data-styled="active" data-styled-version="5.3.11"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_github_catalyst_lib_index_-280e4f-f7d6cfa05e86.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_scroll-anchoring_dist_scroll-anchoring_esm_js-node_modules_github_hydro--09cdca-c8338d3c4dc8.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/app_assets_modules_github_diffs_blob-lines_ts-app_assets_modules_github_diffs_linkable-line-n-b8c0ea-90d580abff98.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/diffs-76da528a8b4c.js.download"></script><style type="text/css" id="ms-consent-banner-theme-styles"></style><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>Add files via upload · Bansodeprasad/Color-Detection-@d2de12d · GitHub</title><meta name="route-pattern" content="/:user_id/:repository/commit/:name(/*path)" data-turbo-transient=""><meta name="route-controller" content="commit" data-turbo-transient=""><meta name="route-action" content="show" data-turbo-transient=""><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="F263:3CAC03:3B339A:4C03FC:67C9462A" data-pjax-transient="true"><meta name="html-safe-nonce" content="821ab99860456582a736aa0195eb222695fd03404c7e86b600000d7b5b7a4951" data-pjax-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9CYW5zb2RlcHJhc2FkL0NvbG9yLURldGVjdGlvbi0iLCJyZXF1ZXN0X2lkIjoiRjI2MzozQ0FDMDM6M0IzMzlBOjRDMDNGQzo2N0M5NDYyQSIsInZpc2l0b3JfaWQiOiI2NjQ2ODg0MDIzMTU3MDk0Njg4IiwicmVnaW9uX2VkZ2UiOiJjZW50cmFsaW5kaWEiLCJyZWdpb25fcmVuZGVyIjoiY2VudHJhbGluZGlhIn0=" data-pjax-transient="true"><meta name="visitor-hmac" content="99def1e36058de3157058567ebcc0fedcc3acc88ec4933b0216d430b66440f9c" data-pjax-transient="true"><meta name="hovercard-subject-tag" content="repository:769861890" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,commits,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_commits" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/commit/show" data-turbo-transient="true"><meta name="user-login" content=""><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><link href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376.diff" rel="alternate" type="text/plain+diff" data-turbo-transient="true"><link href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376.patch" rel="alternate" type="text/plain+patch" data-turbo-transient="true"><meta name="diff-view" content="unified" data-turbo-transient=""><meta name="go-import" content="github.com/Bansodeprasad/Color-Detection- git https://github.com/Bansodeprasad/Color-Detection-.git"><meta name="octolytics-dimension-user_id" content="162862470"><meta name="octolytics-dimension-user_login" content="Bansodeprasad"><meta name="octolytics-dimension-repository_id" content="769861890"><meta name="octolytics-dimension-repository_nwo" content="Bansodeprasad/Color-Detection-"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="769861890"><meta name="octolytics-dimension-repository_network_root_nwo" content="Bansodeprasad/Color-Detection-"><meta name="turbo-body-classes" content="logged-out env-production page-responsive full-width"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><meta name="msapplication-TileImage" content="/windows-tile.png"><meta name="msapplication-TileColor" content="#ffffff"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-out env-production page-responsive full-width" style="overflow-wrap: break-word; --dialog-scrollgutter: 15px;">
    <div data-turbo-body="" class="logged-out env-production page-responsive full-width" style="word-wrap: break-word;">
      


    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#start-of-content" data-skip-target-assigned="false" class="px-2 py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/ui_packages_ui-commands_ui-commands_ts-97496b0f52ba.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/keyboard-shortcuts-dialog-ac448fe050d6.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./color_detection_files/primer-react.694157f711c9f0ff6654.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:r11:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>




      

          

              
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-56e2d9924e94.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./color_detection_files/sessions-730dca81d0a2.js.download"></script>
<header class="HeaderMktg header-logged-out js-details-container js-header Details f4 py-3" role="banner" data-is-top="true" data-color-mode="light" data-light-theme="light" data-dark-theme="dark">
  <h2 class="sr-only">Navigation Menu</h2>

  <button type="button" class="HeaderMktg-backdrop d-lg-none border-0 position-fixed top-0 left-0 width-full height-full js-details-target" aria-label="Toggle navigation">
    <span class="d-none">Toggle navigation</span>
  </button>

  <div class="d-flex flex-column flex-lg-row flex-items-center px-3 px-md-4 px-lg-5 height-full position-relative z-1">
    <div class="d-flex flex-justify-between flex-items-center width-full width-lg-auto">
      <div class="flex-1">
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target js-nav-padding-recalculate js-header-menu-toggle Button--link Button--medium Button d-lg-none color-fg-inherit p-1">  <span class="Button-content">
    <span class="Button-label"><div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div></span>
  </span>
</button>
      </div>

      <a class="mr-lg-3 color-fg-inherit flex-order-2 js-prevent-focus-on-mobile-nav" href="https://github.com/" aria-label="Homepage" data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Logomark;ref_loc:Header&quot;}">
        <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
      </a>

      <div class="flex-1 flex-order-2 text-right">
          <a href="https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FBansodeprasad%2FColor-Detection-%2Fcommit%2Fd2de12dff17aff39101e04671cb502efb8330376" class="HeaderMenu-link HeaderMenu-button d-inline-flex d-lg-none flex-order-1 f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b6249360a433a830f890514b63824addec7db192b2af14ceede8c051f458b170" data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to Sign in&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}">
            Sign in
          </a>
      </div>
    </div>


    <div class="HeaderMenu js-header-menu height-fit position-lg-relative d-lg-flex flex-column flex-auto top-0">
      <div class="HeaderMenu-wrapper d-flex flex-column flex-self-start flex-lg-row flex-auto rounded rounded-lg-0">
          <nav class="HeaderMenu-nav" aria-label="Global">
            <ul class="d-lg-flex list-style-none">
                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Product
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 d-lg-flex flex-wrap dropdown-menu-wide">
          <div class="HeaderMenu-column px-lg-4 border-lg-right mb-4 mb-lg-0 pr-lg-7">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0">
                <ul class="list-style-none f5">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_copilot&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_copilot_link_product_navbar&quot;}" href="https://github.com/features/copilot">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-copilot color-fg-subtle mr-3">
    <path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">GitHub Copilot</div>
        Write better code with AI
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;security&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;security_link_product_navbar&quot;}" href="https://github.com/features/security">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-shield-check color-fg-subtle mr-3">
    <path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Security</div>
        Find and fix vulnerabilities
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;actions&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;actions_link_product_navbar&quot;}" href="https://github.com/features/actions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-workflow color-fg-subtle mr-3">
    <path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Actions</div>
        Automate any workflow
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;codespaces&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;codespaces_link_product_navbar&quot;}" href="https://github.com/features/codespaces">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-codespaces color-fg-subtle mr-3">
    <path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Codespaces</div>
        Instant dev environments
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;issues&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;issues_link_product_navbar&quot;}" href="https://github.com/features/issues">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-issue-opened color-fg-subtle mr-3">
    <path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Zm9.5 2a2 2 0 1 1-.001-3.999A2 2 0 0 1 12 14Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Issues</div>
        Plan and track work
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;code_review&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;code_review_link_product_navbar&quot;}" href="https://github.com/features/code-review">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-code-review color-fg-subtle mr-3">
    <path d="M10.3 6.74a.75.75 0 0 1-.04 1.06l-2.908 2.7 2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M1.5 4.25c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v12.5a1.75 1.75 0 0 1-1.75 1.75h-9.69l-3.573 3.573A1.458 1.458 0 0 1 5 21.043V18.5H3.25a1.75 1.75 0 0 1-1.75-1.75ZM3.25 4a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h2.5a.75.75 0 0 1 .75.75v3.19l3.72-3.72a.749.749 0 0 1 .53-.22h10a.25.25 0 0 0 .25-.25V4.25a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Code Review</div>
        Manage code changes
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;discussions&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;discussions_link_product_navbar&quot;}" href="https://github.com/features/discussions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-comment-discussion color-fg-subtle mr-3">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Discussions</div>
        Collaborate outside of code
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;code_search&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;code_search_link_product_navbar&quot;}" href="https://github.com/features/code-search">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-code-square color-fg-subtle mr-3">
    <path d="M10.3 8.24a.75.75 0 0 1-.04 1.06L7.352 12l2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M2 3.75C2 2.784 2.784 2 3.75 2h16.5c.966 0 1.75.784 1.75 1.75v16.5A1.75 1.75 0 0 1 20.25 22H3.75A1.75 1.75 0 0 1 2 20.25Zm1.75-.25a.25.25 0 0 0-.25.25v16.5c0 .138.112.25.25.25h16.5a.25.25 0 0 0 .25-.25V3.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Code Search</div>
        Find more, search less
      </div>

    
</a></li>

                </ul>
              </div>
          </div>
          <div class="HeaderMenu-column px-lg-4">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0 border-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="product-explore-heading">Explore</span>
                <ul class="list-style-none f5" aria-labelledby="product-explore-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;all_features&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;all_features_link_product_navbar&quot;}" href="https://github.com/features">
      All features

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;documentation&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;documentation_link_product_navbar&quot;}" href="https://docs.github.com/">
      Documentation

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_skills&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_skills_link_product_navbar&quot;}" href="https://skills.github.com/">
      GitHub Skills

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;blog&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;blog_link_product_navbar&quot;}" href="https://github.blog/">
      Blog

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                </ul>
              </div>
          </div>
      </div>
</li>

                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Solutions
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 d-lg-flex flex-wrap dropdown-menu-wide">
          <div class="HeaderMenu-column px-lg-4 border-lg-right mb-4 mb-lg-0 pr-lg-7">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0 pb-lg-3 mb-3 mb-lg-0">
                    <span class="d-block h4 color-fg-default my-1" id="solutions-by-company-size-heading">By company size</span>
                <ul class="list-style-none f5" aria-labelledby="solutions-by-company-size-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;enterprises&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;enterprises_link_solutions_navbar&quot;}" href="https://github.com/enterprise">
      Enterprises

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;small_and_medium_teams&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;small_and_medium_teams_link_solutions_navbar&quot;}" href="https://github.com/team">
      Small and medium teams

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;startups&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;startups_link_solutions_navbar&quot;}" href="https://github.com/enterprise/startups">
      Startups

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;nonprofits&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;nonprofits_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/nonprofits">
      Nonprofits

    
</a></li>

                </ul>
              </div>
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="solutions-by-use-case-heading">By use case</span>
                <ul class="list-style-none f5" aria-labelledby="solutions-by-use-case-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devsecops&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devsecops_link_solutions_navbar&quot;}" href="https://github.com/solutions/use-case/devsecops">
      DevSecOps

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devops&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devops_link_solutions_navbar&quot;}" href="https://github.com/solutions/use-case/devops">
      DevOps

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;ci_cd&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;ci_cd_link_solutions_navbar&quot;}" href="https://github.com/solutions/use-case/ci-cd">
      CI/CD

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all_use_cases&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_use_cases_link_solutions_navbar&quot;}" href="https://github.com/solutions/use-case">
      View all use cases

    
</a></li>

                </ul>
              </div>
          </div>
          <div class="HeaderMenu-column px-lg-4">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="solutions-by-industry-heading">By industry</span>
                <ul class="list-style-none f5" aria-labelledby="solutions-by-industry-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;healthcare&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;healthcare_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/healthcare">
      Healthcare

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;financial_services&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;financial_services_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/financial-services">
      Financial services

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;manufacturing&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;manufacturing_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/manufacturing">
      Manufacturing

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;government&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;government_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/government">
      Government

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all_industries&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_industries_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry">
      View all industries

    
</a></li>

                </ul>
              </div>
          </div>
         <div class="HeaderMenu-trailing-link rounded-bottom-2 flex-shrink-0 mt-lg-4 px-lg-4 py-4 py-lg-3 f5 text-semibold">
            <a href="https://github.com/solutions">
              View all solutions
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right HeaderMenu-trailing-link-icon">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</a>         </div>
      </div>
</li>

                    <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Resources
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 d-lg-flex flex-wrap dropdown-menu-wide">
          <div class="HeaderMenu-column px-lg-4 border-lg-right mb-4 mb-lg-0 pr-lg-7">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="resources-topics-heading">Topics</span>
                <ul class="list-style-none f5" aria-labelledby="resources-topics-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;ai&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;ai_link_resources_navbar&quot;}" href="https://github.com/resources/articles/ai">
      AI

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devops&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devops_link_resources_navbar&quot;}" href="https://github.com/resources/articles/devops">
      DevOps

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;security&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;security_link_resources_navbar&quot;}" href="https://github.com/resources/articles/security">
      Security

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;software_development&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;software_development_link_resources_navbar&quot;}" href="https://github.com/resources/articles/software-development">
      Software Development

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_link_resources_navbar&quot;}" href="https://github.com/resources/articles">
      View all

    
</a></li>

                </ul>
              </div>
          </div>
          <div class="HeaderMenu-column px-lg-4">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0 border-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="resources-explore-heading">Explore</span>
                <ul class="list-style-none f5" aria-labelledby="resources-explore-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;learning_pathways&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;learning_pathways_link_resources_navbar&quot;}" href="https://resources.github.com/learn/pathways">
      Learning Pathways

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;events_amp_webinars&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;events_amp_webinars_link_resources_navbar&quot;}" href="https://resources.github.com/">
      Events &amp; Webinars

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;ebooks_amp_whitepapers&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;ebooks_amp_whitepapers_link_resources_navbar&quot;}" href="https://github.com/resources/whitepapers">
      Ebooks &amp; Whitepapers

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;customer_stories&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;customer_stories_link_resources_navbar&quot;}" href="https://github.com/customer-stories">
      Customer Stories

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;partners&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;partners_link_resources_navbar&quot;}" href="https://partner.github.com/">
      Partners

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;executive_insights&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;executive_insights_link_resources_navbar&quot;}" href="https://github.com/solutions/executive-insights">
      Executive Insights

    
</a></li>

                </ul>
              </div>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Open Source
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 px-lg-4">
          <div class="HeaderMenu-column">
              <div class="border-bottom pb-3 pb-lg-0 pb-lg-3 mb-3 mb-lg-0 mb-lg-3">
                <ul class="list-style-none f5">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_sponsors&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_sponsors_link_open_source_navbar&quot;}" href="https://github.com/sponsors">
      
      <div>
        <div class="color-fg-default h4">GitHub Sponsors</div>
        Fund open source developers
      </div>

    
</a></li>

                </ul>
              </div>
              <div class="border-bottom pb-3 pb-lg-0 pb-lg-3 mb-3 mb-lg-0 mb-lg-3">
                <ul class="list-style-none f5">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;the_readme_project&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;the_readme_project_link_open_source_navbar&quot;}" href="https://github.com/readme">
      
      <div>
        <div class="color-fg-default h4">The ReadME Project</div>
        GitHub community articles
      </div>

    
</a></li>

                </ul>
              </div>
              <div class="border-bottom pb-3 pb-lg-0 border-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="open-source-repositories-heading">Repositories</span>
                <ul class="list-style-none f5" aria-labelledby="open-source-repositories-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;topics&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;topics_link_open_source_navbar&quot;}" href="https://github.com/topics">
      Topics

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;trending&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;trending_link_open_source_navbar&quot;}" href="https://github.com/trending">
      Trending

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;collections&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;collections_link_open_source_navbar&quot;}" href="https://github.com/collections">
      Collections

    
</a></li>

                </ul>
              </div>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Enterprise
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 px-lg-4">
          <div class="HeaderMenu-column">
              <div class="border-bottom pb-3 pb-lg-0 pb-lg-3 mb-3 mb-lg-0 mb-lg-3">
                <ul class="list-style-none f5">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;enterprise_platform&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;enterprise_platform_link_enterprise_navbar&quot;}" href="https://github.com/enterprise">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-stack color-fg-subtle mr-3">
    <path d="M11.063 1.456a1.749 1.749 0 0 1 1.874 0l8.383 5.316a1.751 1.751 0 0 1 0 2.956l-8.383 5.316a1.749 1.749 0 0 1-1.874 0L2.68 9.728a1.751 1.751 0 0 1 0-2.956Zm1.071 1.267a.25.25 0 0 0-.268 0L3.483 8.039a.25.25 0 0 0 0 .422l8.383 5.316a.25.25 0 0 0 .268 0l8.383-5.316a.25.25 0 0 0 0-.422Z"></path><path d="M1.867 12.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path><path d="M1.867 16.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Enterprise platform</div>
        AI-powered developer platform
      </div>

    
</a></li>

                </ul>
              </div>
              <div class="border-bottom pb-3 pb-lg-0 border-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="enterprise-available-add-ons-heading">Available add-ons</span>
                <ul class="list-style-none f5" aria-labelledby="enterprise-available-add-ons-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;advanced_security&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;advanced_security_link_enterprise_navbar&quot;}" href="https://github.com/enterprise/advanced-security">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-shield-check color-fg-subtle mr-3">
    <path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Advanced Security</div>
        Enterprise-grade security features
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;copilot_for_business&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;copilot_for_business_link_enterprise_navbar&quot;}" href="https://github.com/features/copilot/copilot-business">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-copilot color-fg-subtle mr-3">
    <path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Copilot for business</div>
        Enterprise-grade AI features
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;premium_support&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;premium_support_link_enterprise_navbar&quot;}" href="https://github.com/premium-support">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-comment-discussion color-fg-subtle mr-3">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Premium Support</div>
        Enterprise-grade 24/7 support
      </div>

    
</a></li>

                </ul>
              </div>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
    <a class="HeaderMenu-link no-underline px-0 px-lg-2 py-3 py-lg-2 d-block d-lg-inline-block" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;pricing&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;pricing_link_global_navbar&quot;}" href="https://github.com/pricing">Pricing</a>
</li>

            </ul>
          </nav>

        <div class="d-flex flex-column flex-lg-row width-full flex-justify-end flex-lg-items-center text-center mt-3 mt-lg-0 text-lg-left ml-lg-3">
                


<qbsearch-input class="search-input" data-scope="repo:Bansodeprasad/Color-Detection-" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="LBIADeU7gChOOmB7WAwlE0_799PD5EiCyLVYOgjMLc0ds7qLPZLsbEmTVgfoTQY4CNcgMqtUCO755s98CwfZiA" data-max-custom-scopes="10" data-header-redesign-enabled="false" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="Bansodeprasad/Color-Detection-" data-current-org="" data-current-owner="Bansodeprasad" data-logged-in="false" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-retain-scroll-position="true" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center mr-4 rounded" data-action="click:qbsearch-input#searchInputContainerClicked">
      <button type="button" class="header-search-button placeholder input-button form-control d-flex flex-1 flex-self-stretch flex-items-center no-wrap width-full py-0 pl-2 pr-0 text-left border-0 box-shadow-none" data-target="qbsearch-input.inputButton" aria-label="Search or jump to…" aria-haspopup="dialog" placeholder="Search or jump to..." data-hotkey="s,/" autocapitalize="off" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}" data-action="click:qbsearch-input#handleExpand">
        <div class="mr-2 color-fg-muted">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <span class="flex-1" data-target="qbsearch-input.inputButtonText">Search or jump to...</span>
          <div class="d-flex" data-target="qbsearch-input.hotkeyIndicator">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="20" aria-hidden="true" class="mr-1"><path fill="none" stroke="#979A9C" opacity=".4" d="M3.5.5h12c1.7 0 3 1.3 3 3v13c0 1.7-1.3 3-3 3h-12c-1.7 0-3-1.3-3-3v-13c0-1.7 1.3-3 3-3z"></path><path fill="#979A9C" d="M11.8 6L8 15.1h-.9L10.8 6h1z"></path></svg>

          </div>
      </button>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-large Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-fixed width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-f1beaaca-ecd6-414a-b7c1-8f2b4c3dc642" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-f1beaaca-ecd6-414a-b7c1-8f2b4c3dc642" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="Xm3hwHr1PXFAhx1sRsQ4P186HK3L59zZuVr3sgok1QZIu81f1uBQLxhNTkpxJLubDNvFnWLURGHyZKIX1h1NMw==">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="4cyqpBiapwD9CBho+a1CoG1Wg3tCVQfOUk7KF32dQMMpdRiy0xGVlc3RWemRZi8asQo1esreJDKBIfy1N1KYJg==">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="" only-validate-on-blur="false">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" data-csrf="true" value="fe0/DKPaQqrT+m8iTYBir2I3oXSo5n8nsTD+DZvwdILnkxePLq/QLyTbtjke/E5ZUUjJtUKdOeYBslNeOIGN7g==">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>


            <div class="position-relative HeaderMenu-link-wrap d-lg-inline-block">
              <a href="https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FBansodeprasad%2FColor-Detection-%2Fcommit%2Fd2de12dff17aff39101e04671cb502efb8330376" class="HeaderMenu-link HeaderMenu-link--sign-in HeaderMenu-button flex-shrink-0 no-underline d-none d-lg-inline-flex border border-lg-0 rounded rounded-lg-0 px-2 py-1" style="margin-left: 12px;" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b6249360a433a830f890514b63824addec7db192b2af14ceede8c051f458b170" data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}">
                Sign in
              </a>
            </div>

              <a href="https://github.com/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fcommit%2Fshow&amp;source=header-repo&amp;source_repo=Bansodeprasad%2FColor-Detection-" class="HeaderMenu-link HeaderMenu-link--sign-up HeaderMenu-button flex-shrink-0 d-flex d-lg-inline-flex no-underline border color-border-default rounded px-2 py-1" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b6249360a433a830f890514b63824addec7db192b2af14ceede8c051f458b170" data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/commit/show;ref_cta:Sign up;ref_loc:header logged out&quot;}">
                Sign up
              </a>
          <button type="button" class="sr-only js-header-menu-focus-trap d-block d-lg-none">Reseting focus</button>
        </div>
      </div>
    </div>
  </div>
</header>

      <div data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376">Reload</a> to refresh your session.</span>

    <button id="icon-button-5ccd85aa-d5fa-416d-9bbb-d3eadbf4cf2d" aria-labelledby="tooltip-1c681ff9-6246-402d-84c8-9596658a2e9c" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-1c681ff9-6246-402d-84c8-9596658a2e9c" for="icon-button-5ccd85aa-d5fa-416d-9bbb-d3eadbf4cf2d" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
  
    






  
  <div id="repository-container-header" class="pt-3 hide-full-screen" style="background-color: var(--page-header-bgColor, var(--color-page-header-bg));" data-turbo-replace="">

      <div class="d-flex flex-nowrap flex-justify-end mb-3  px-3 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit">
            
  <div class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo color-fg-muted mr-2">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
    
    <span class="author flex-self-stretch" itemprop="author">
      <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/Bansodeprasad/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Bansodeprasad">
        Bansodeprasad
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="https://github.com/Bansodeprasad/Color-Detection-">Color-Detection-</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
  </div>


        </div>

        <div id="repository-details-container" class="flex-shrink-0" data-turbo-replace="" style="max-width: 70%;">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      

  <li>
            <a href="https://github.com/login?return_to=%2FBansodeprasad%2FColor-Detection-" rel="nofollow" id="repository-details-watch-button" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ef5ab0c9d320fa1f7f63e5625bf6999667fd091bae31b13deb59bc077109042a" aria-label="You must be signed in to change notification settings" data-view-component="true" class="btn-sm btn" aria-describedby="tooltip-6afa1895-5fc1-4f07-9d65-47dd0b11ebd0">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>    <tool-tip id="tooltip-6afa1895-5fc1-4f07-9d65-47dd0b11ebd0" for="repository-details-watch-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="position-absolute sr-only" role="tooltip" style="--tool-tip-position-top: 116px; --tool-tip-position-left: 1080.1015625px;"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You must be signed in to change notification settings</tool-tip>

  </li>

  <li>
          <a icon="repo-forked" id="fork-button" href="https://github.com/login?return_to=%2FBansodeprasad%2FColor-Detection-" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:769861890,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="441e6743d32f22e1fbdc565e3d9e229ee21084149f93ba36ceb449a327252e11" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="3" data-view-component="true" class="Counter">3</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="https://github.com/login?return_to=%2FBansodeprasad%2FColor-Detection-" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:769861890,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="8c046a4e086732b9e3a179d9db9d01cb12047dfda51c5939d86200afbee171bc" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-sw btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="2 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="2" data-view-component="true" class="Counter js-social-count">2</span>
</a></div>
  </li>

</ul>

        </div>
      </div>

        <div id="responsive-meta-container" data-turbo-replace="">
</div>


          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/Bansodeprasad/Color-Detection-" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /Bansodeprasad/Color-Detection-" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/Bansodeprasad/Color-Detection-/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /Bansodeprasad/Color-Detection-/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/Bansodeprasad/Color-Detection-/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /Bansodeprasad/Color-Detection-/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="2" data-view-component="true" class="Counter">2</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/Bansodeprasad/Color-Detection-/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /Bansodeprasad/Color-Detection-/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/Bansodeprasad/Color-Detection-/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /Bansodeprasad/Color-Detection-/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/Bansodeprasad/Color-Detection-/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /Bansodeprasad/Color-Detection-/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/Bansodeprasad/Color-Detection-/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /Bansodeprasad/Color-Detection-/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="" data-ready="true">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-e4029d67-6923-4ae6-a98e-49108ca156e8-button" popovertarget="action-menu-e4029d67-6923-4ae6-a98e-49108ca156e8-overlay" aria-controls="action-menu-e4029d67-6923-4ae6-a98e-49108ca156e8-list" aria-haspopup="true" aria-labelledby="tooltip-3753d92f-110e-4071-997d-36496e025fd8" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-3753d92f-110e-4071-997d-36496e025fd8" for="action-menu-e4029d67-6923-4ae6-a98e-49108ca156e8-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-e4029d67-6923-4ae6-a98e-49108ca156e8-overlay" anchor="action-menu-e4029d67-6923-4ae6-a98e-49108ca156e8-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-e4029d67-6923-4ae6-a98e-49108ca156e8-button" id="action-menu-e4029d67-6923-4ae6-a98e-49108ca156e8-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-77fbd23c-a90d-411c-82db-dc10567345b1" href="https://github.com/Bansodeprasad/Color-Detection-" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-bf8e57dc-0338-4bd8-81d8-e8cf46caa171" href="https://github.com/Bansodeprasad/Color-Detection-/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-13bab11a-fff8-40f9-b01a-06112cf1d0ce" href="https://github.com/Bansodeprasad/Color-Detection-/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-e4c13518-b681-41fd-9c32-85b0730431ff" href="https://github.com/Bansodeprasad/Color-Detection-/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-5dc6e671-f16d-4cf7-98c1-03c40b0a8b29" href="https://github.com/Bansodeprasad/Color-Detection-/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-0f8e4555-1fdb-4959-9d49-6e66a40a2ac6" href="https://github.com/Bansodeprasad/Color-Detection-/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-ee82949d-edb6-42d3-be30-8f3846b20d4c" href="https://github.com/Bansodeprasad/Color-Detection-/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>

  </div>

  



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
    



    
      
<div class="clearfix mt-4 px-3 px-md-4 px-lg-5">
  <div class="Subhead">
  <h2 class="Subhead-heading">Commit</h2>
</div>

<a href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>




<div id="spoof-warning" class="mt-0 pb-3" hidden="" aria-hidden="">
  <div data-view-component="true" class="flash flash-warn mt-0 clearfix">
  
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert float-left mt-1">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>

      <div class="overflow-hidden">This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.</div>


  
</div></div>


<div class="commit full-commit mt-0 px-2 pt-2 ">
  <div class="d-flex flex-justify-between gap-2">
    <div class="d-flex">
        <span class="mr-1" style="height: 24px">
        </span>

        <div class="commit-title markdown-title">
          Add files via upload
        </div>
    </div>

    <a id="browse-at-time-link" href="https://github.com/Bansodeprasad/Color-Detection-/tree/d2de12dff17aff39101e04671cb502efb8330376" class="btn flex-self-start" rel="nofollow" aria-describedby="tooltip-18a12d8c-5c56-4018-9337-307bc7760c6d">Browse files</a>
    <tool-tip id="tooltip-18a12d8c-5c56-4018-9337-307bc7760c6d" for="browse-at-time-link" popover="manual" data-direction="ne" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Browse the repository at this point in the history</tool-tip>
  </div>


  <div class="commit-branches pb-2">
  

    <div class="pt-2">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch">
    <path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path>
</svg>
      <ul class="branches-list">
          <li class="branch"><a href="https://github.com/Bansodeprasad/Color-Detection-">main</a></li>
      </ul>
    </div>
</div>


  <div class="commit-meta p-2 d-flex flex-wrap gap-3 flex-column flex-md-row">

    <div class="d-flex flex-1">
      
<div class="AvatarStack flex-self-start  ">
  <div class="AvatarStack-body">
      <a class="avatar avatar-user" style="width:20px;height:20px;" data-test-selector="commits-avatar-stack-avatar-link" data-hovercard-type="user" data-hovercard-url="/users/Bansodeprasad/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Bansodeprasad">
        <img data-test-selector="commits-avatar-stack-avatar-image" src="./color_detection_files/162862470" width="20" height="20" alt="@Bansodeprasad" class=" avatar-user">
</a>  </div>
</div>

      <div class="flex-self-start flex-content-center">
            <a class="commit-author user-mention" title="View all commits by Bansodeprasad" data-hovercard-type="user" data-hovercard-url="/users/Bansodeprasad/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Bansodeprasad/Color-Detection-/commits?author=Bansodeprasad">Bansodeprasad</a>
    
  authored
  <relative-time datetime="2024-03-10T09:25:54Z" class="no-wrap" title="Mar 10, 2024, 2:55 PM GMT+5:30"><template shadowrootmode="open">on Mar 10, 2024</template>Mar 10, 2024</relative-time>

        <div class="d-none d-md-inline-block">
          

    <button id="dialog-show-commit-badge-verified-e446f7e1-dialog" data-show-dialog-id="commit-badge-verified-e446f7e1-dialog" type="button" data-view-component="true" class="signed-commit-badge signed-commit-badge-medium verified  Button--secondary Button--medium Button">  <span class="Button-content">
    <span class="Button-label">Verified</span>
  </span>
</button>

<dialog-helper>
  <dialog id="commit-badge-verified-e446f7e1-dialog" aria-modal="true" aria-labelledby="commit-badge-verified-e446f7e1-dialog-title" aria-describedby="commit-badge-verified-e446f7e1-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--disableScroll">
    <div style="border-radius: 12px 12px 0 0" data-view-component="true" class="Overlay-header Overlay-header--divided color-bg-subtle">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="commit-badge-verified-e446f7e1-dialog-title">
        Verified
      </h1>
                <div class="d-flex">
          <div class="pr-1">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-verified mr-2 color-fg-success">
    <path d="m9.585.52.929.68c.153.112.331.186.518.215l1.138.175a2.678 2.678 0 0 1 2.24 2.24l.174 1.139c.029.187.103.365.215.518l.68.928a2.677 2.677 0 0 1 0 3.17l-.68.928a1.174 1.174 0 0 0-.215.518l-.175 1.138a2.678 2.678 0 0 1-2.241 2.241l-1.138.175a1.17 1.17 0 0 0-.518.215l-.928.68a2.677 2.677 0 0 1-3.17 0l-.928-.68a1.174 1.174 0 0 0-.518-.215L3.83 14.41a2.678 2.678 0 0 1-2.24-2.24l-.175-1.138a1.17 1.17 0 0 0-.215-.518l-.68-.928a2.677 2.677 0 0 1 0-3.17l.68-.928c.112-.153.186-.331.215-.518l.175-1.14a2.678 2.678 0 0 1 2.24-2.24l1.139-.175c.187-.029.365-.103.518-.215l.928-.68a2.677 2.677 0 0 1 3.17 0ZM7.303 1.728l-.927.68a2.67 2.67 0 0 1-1.18.489l-1.137.174a1.179 1.179 0 0 0-.987.987l-.174 1.136a2.677 2.677 0 0 1-.489 1.18l-.68.928a1.18 1.18 0 0 0 0 1.394l.68.927c.256.348.424.753.489 1.18l.174 1.137c.078.509.478.909.987.987l1.136.174a2.67 2.67 0 0 1 1.18.489l.928.68c.414.305.979.305 1.394 0l.927-.68a2.67 2.67 0 0 1 1.18-.489l1.137-.174a1.18 1.18 0 0 0 .987-.987l.174-1.136a2.67 2.67 0 0 1 .489-1.18l.68-.928a1.176 1.176 0 0 0 0-1.394l-.68-.927a2.686 2.686 0 0 1-.489-1.18l-.174-1.137a1.179 1.179 0 0 0-.987-.987l-1.136-.174a2.677 2.677 0 0 1-1.18-.489l-.928-.68a1.176 1.176 0 0 0-1.394 0ZM11.28 6.78l-3.75 3.75a.75.75 0 0 1-1.06 0L4.72 8.78a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L7 8.94l3.22-3.22a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
          </div>
          <div class="flex-1">
                This commit was created on GitHub.com and signed with GitHub’s <strong class="color-fg-success">verified signature</strong>.
          </div>
        </div>

    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="commit-badge-verified-e446f7e1-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="commit-badge-verified-e446f7e1-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div class="signed-commit-footer">
            <span class="d-block">GPG key ID: <span class="color-fg-muted">B5690EEEBB952194</span></span>
            <div class="my-1">
            </div>
            <div>Verified
              <relative-time datetime="2024-11-18 20:54:29 +0530" threshold="PT0S" year="numeric" hour="2-digit" minute="2-digit" title="Nov 18, 2024, 8:54 PM GMT+5:30"><template shadowrootmode="open">on Nov 18, 2024, 08:54 PM</template></relative-time>
            </div>
          <a class="Link--inTextBlock" href="https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits">Learn about vigilant mode</a>
        </div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>

        </div>
      </div>
    </div>

    <div class="d-flex gap-3 no-wrap text-lg-right text-left overflow-x-auto">
      <span class="sha-block ml-0" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
        1 parent
          
          <a class="sha" data-hotkey="p" href="https://github.com/Bansodeprasad/Color-Detection-/commit/1724f953f3d24296dd1c1c2d1193328460a204ed" data-turbo-frame="repo-content-turbo-frame">1724f95</a>
      </span>
      <span class="sha-block m-0">commit <span class="sha user-select-contain">d2de12d</span></span>
    </div>
  </div>
</div>


  


  <diff-layout data-catalyst="">
    <div class="pr-toolbar commit-toolbar mt-n2 color-bg-default d-flex js-sticky-offset-scroll" data-target="diff-layout.diffToolbar">
        <div id="toc" class="d-flex flex-items-center js-details-container Details flex-1 my-2" style="gap: 4px 16px;">
  <file-tree-toggle data-action="toggle-sidebar:diff-layout#toggleSidebar" class="d-none d-md-inline-block d-lg-inline-block d-xl-inline-block" data-catalyst="" data-url="" data-csrf="">
    <div data-view-component="true" class="position-relative d-inline-block">
    <button id="show-file-tree-button" data-target="file-tree-toggle.showFileTreeButton diff-layout.showFileTreeButton" data-action="click:file-tree-toggle#toggleFileTree" data-prefer-file-tree-visible="true" data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;show_tree&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="029bf1fd06f09671b2a4d9cca70e90c635048b866091fd9aa1e880e7843f947b" hidden="hidden" type="button" data-view-component="true" class="btn-octicon Link--muted diffbar-item m-0 p-0" aria-labelledby="tooltip-7d4d8467-f620-4610-ba51-00d3c1c46f55">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sidebar-collapse">
    <path d="M6.823 7.823a.25.25 0 0 1 0 .354l-2.396 2.396A.25.25 0 0 1 4 10.396V5.604a.25.25 0 0 1 .427-.177Z"></path><path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25H9.5v-13H1.75a.25.25 0 0 0-.25.25ZM11 14.5h3.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11Z"></path>
</svg>
</button>    <tool-tip id="tooltip-7d4d8467-f620-4610-ba51-00d3c1c46f55" for="show-file-tree-button" popover="manual" data-direction="ne" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Show file tree</tool-tip>
</div>

    <div data-view-component="true" class="position-relative d-inline-block">
    <button id="hide-file-tree-button" data-target="file-tree-toggle.hideFileTreeButton" data-action="click:file-tree-toggle#toggleFileTree" data-prefer-file-tree-visible="false" data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;hide_tree&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="05b1f0c27ca69d82be9dcd83e4085e89baaf6af5fe8110dc5161d7ff93a50b8a" type="button" data-view-component="true" class="btn-octicon Link--muted diffbar-item m-0 p-0" aria-labelledby="tooltip-d4736c9f-1b56-47c4-9cfd-4110db671dcc">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sidebar-expand">
    <path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path>
</svg>
</button>    <tool-tip id="tooltip-d4736c9f-1b56-47c4-9cfd-4110db671dcc" for="hide-file-tree-button" popover="manual" data-direction="ne" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Hide file tree</tool-tip>
</div>
</file-tree-toggle>


    <div>
      Showing
      <strong>6 changed files</strong>
      with
      <strong>934 additions</strong>
      and
      <strong>0 deletions</strong>.
    </div>

  <div class="flex-1"></div>
  <div class="d-flex d-inline-block">
    <!-- '"` --><!-- </textarea></xmp> --><form class="d-flex gap-2 flex-column flex-sm-row flex-items-end" data-turbo="false" action="https://github.com/users/diffview" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="5eq3Rgm7DEUbniTCQPPBbh915zCdqCEemfaxrRP94FAaMjf0bZ+H/fYAE0TJQxKKaB9QSk4xUBKUjPJeYVoslw==">
      <segmented-control data-catalyst="">
  <ul aria-label="Whitespace" role="list" data-view-component="true" class="SegmentedControl--small SegmentedControl">
      <li class="SegmentedControl-item SegmentedControl-item--selected" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="w" value="0" data-action="click:segmented-control#select" aria-current="true" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Whitespace">Whitespace</span>
  </span>
</button>

</li>

      <li class="SegmentedControl-item" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="w" value="1" data-action="click:segmented-control#select" aria-current="false" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Ignore whitespace">Ignore whitespace</span>
  </span>
</button>

</li>

</ul></segmented-control>
      <segmented-control data-catalyst="">
  <ul aria-label="Diff view" role="list" data-view-component="true" class="SegmentedControl--small SegmentedControl">
      <li class="SegmentedControl-item" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="diff" value="split" data-action="click:segmented-control#select" aria-current="false" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Split">Split</span>
  </span>
</button>

</li>

      <li class="SegmentedControl-item SegmentedControl-item--selected" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="diff" value="unified" data-action="click:segmented-control#select" aria-current="true" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Unified">Unified</span>
  </span>
</button>

</li>

</ul></segmented-control>
      <input type="hidden" name="old_w" id="old_w" value="0" autocomplete="off" class="form-control">
      <input type="hidden" name="old_diff" id="old_diff" value="unified" autocomplete="off" class="form-control">
</form>  </div>
</div>

    </div>
      <div side="left" responsive="true" data-target="diff-layout.layoutContainer" data-view-component="true" class="Layout Layout--flowRow-until-md Layout--gutter-condensed  hx_Layout wants-full-width-container Layout--sidebarPosition-start Layout--sidebarPosition-flowRow-none">
  
  <div data-target="diff-layout.sidebarContainer" data-action="scroll:diff-layout.sidebarContainer#handleSidebarScroll" data-view-component="true" class="Layout-sidebar overflow-y-auto hx_Layout--sidebar js-notification-shelf-offset-top diff-sidebar position-sticky p-2" data-original-top="60px" style="top: 60px !important; height: 366px;">            <div>
              <svg xmlns="http://www.w3.org/2000/svg" hidden="" aria-hidden="true">
  <symbol id="octicon_file-directory-fill_16" viewBox="0 0 16 16" width="16" height="16"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></symbol><symbol id="octicon_file-submodule_16" viewBox="0 0 16 16" width="16" height="16"><path d="M0 2.75C0 1.784.784 1 1.75 1H5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1h6.75c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25Zm9.42 9.36 2.883-2.677a.25.25 0 0 0 0-.366L9.42 6.39a.249.249 0 0 0-.42.183V8.5H4.75a.75.75 0 0 0 0 1.5H9v1.927c0 .218.26.331.42.183Z"></path></symbol><symbol id="octicon_file_16" viewBox="0 0 16 16" width="16" height="16"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></symbol><symbol id="octicon_chevron-down_16" viewBox="0 0 16 16" width="16" height="16"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></symbol><symbol id="octicon_diff-added_16" viewBox="0 0 16 16" width="16" height="16"><path d="M2.75 1h10.5c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 15H2.75A1.75 1.75 0 0 1 1 13.25V2.75C1 1.784 1.784 1 2.75 1Zm10.5 1.5H2.75a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25ZM8 4a.75.75 0 0 1 .75.75v2.5h2.5a.75.75 0 0 1 0 1.5h-2.5v2.5a.75.75 0 0 1-1.5 0v-2.5h-2.5a.75.75 0 0 1 0-1.5h2.5v-2.5A.75.75 0 0 1 8 4Z"></path></symbol><symbol id="octicon_diff-removed_16" viewBox="0 0 16 16" width="16" height="16"><path d="M13.25 1c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 15H2.75A1.75 1.75 0 0 1 1 13.25V2.75C1 1.784 1.784 1 2.75 1ZM2.75 2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25Zm8.5 6.25h-6.5a.75.75 0 0 1 0-1.5h6.5a.75.75 0 0 1 0 1.5Z"></path></symbol><symbol id="octicon_diff-modified_16" viewBox="0 0 16 16" width="16" height="16"><path d="M13.25 1c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 15H2.75A1.75 1.75 0 0 1 1 13.25V2.75C1 1.784 1.784 1 2.75 1ZM2.75 2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path></symbol><symbol id="octicon_diff-renamed_16" viewBox="0 0 16 16" width="16" height="16"><path d="M13.25 1c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 15H2.75A1.75 1.75 0 0 1 1 13.25V2.75C1 1.784 1.784 1 2.75 1ZM2.75 2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25Zm9.03 6.03-3.25 3.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.97-1.97H4.75a.75.75 0 0 1 0-1.5h4.69L7.47 5.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018l3.25 3.25a.75.75 0 0 1 0 1.06Z"></path></symbol>
</svg>


<div class="subnav-search mx-0 mb-2">
  <input type="text" id="file-tree-filter-field" class="form-control input-block pl-5 js-filterable-field" placeholder="Filter changed files" aria-label="Filter changed files" autocomplete="off" data-target="diff-layout.fileTreePathFilter" data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_filter&quot;,&quot;data&quot;:{&quot;file_count&quot;:6},&quot;pull_request_id&quot;:&quot;d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null,&quot;action&quot;:&quot;filter_by_pathname&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;}}" data-hydro-click-hmac="a7f87f02eee6b2e69efb12f0c80f266baae23c8b7823b7fe928d9dd3c8517b19">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search subnav-search-icon">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
</div>
<experimental-action-list data-arrow-navigation="true" data-catalyst="">
  <file-tree data-target="diff-layout.fileTree" data-catalyst="">
    <nav aria-label="File Tree Navigation">
      <ul class="ActionList ActionList--tree ActionList--full" role="tree" aria-label="File Tree" data-filterable-for="file-tree-filter-field" data-filterable-type="substring" data-tree-entry-type="root" data-target="diff-file-filter.treeRoot" data-action="
          filterable:change:diff-file-filter#hideEmptyDirectories
          filterable:change:file-tree#instrumentPathFilterChange
          filterable:change:experimental-action-list#setupFocusZone
        ">
            <li id="file-tree-item-diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4" class="ActionList-item js-tree-node ActionList-item--navActive" role="treeitem" aria-level="1" style="--ActionList-tree-depth: 1;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:6,&quot;path&quot;:&quot;color_detection.py&quot;,&quot;extension&quot;:&quot;.py&quot;},&quot;pull_request_id&quot;:&quot;d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;}}" data-hydro-click-hmac="f2059fbb72882f917af91919d60015bdaf1681889876db76ec0df8bbb97a3a48" data-file-type=".py" data-file-deleted="false" data-tree-entry-type="file" data-hydro-client-context="{&quot;tree_file_count&quot;:6}" aria-current="location">
    <span data-filterable-item-text="" hidden="">color_detection.py</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4" data-turbo="false" tabindex="0">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        color_detection.py
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

            <li id="file-tree-item-diff-d25b26e0206934607c80f8323f24c3de320a322ba8893f7d05f3bb791f9013b9" class="ActionList-item js-tree-node" role="treeitem" aria-level="1" style="--ActionList-tree-depth: 1;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:6,&quot;path&quot;:&quot;colorpic.jpg&quot;,&quot;extension&quot;:&quot;.jpg&quot;},&quot;pull_request_id&quot;:&quot;d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;}}" data-hydro-click-hmac="82d329a69946003bcea7a0d7ec8ecf82d3b96c457a00d337ba00dc5259c7df4a" data-file-type=".jpg" data-file-deleted="false" data-tree-entry-type="file" data-hydro-client-context="{&quot;tree_file_count&quot;:6}">
    <span data-filterable-item-text="" hidden="">colorpic.jpg</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-d25b26e0206934607c80f8323f24c3de320a322ba8893f7d05f3bb791f9013b9" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        colorpic.jpg
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

            <li id="file-tree-item-diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604" class="ActionList-item js-tree-node" role="treeitem" aria-level="1" style="--ActionList-tree-depth: 1;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:6,&quot;path&quot;:&quot;colors.csv&quot;,&quot;extension&quot;:&quot;.csv&quot;},&quot;pull_request_id&quot;:&quot;d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;}}" data-hydro-click-hmac="418a8c7d4712e5bed151c19824fa0bd2c13435b07eebacf53f3482cc6adeaf58" data-file-type=".csv" data-file-deleted="false" data-tree-entry-type="file" data-hydro-client-context="{&quot;tree_file_count&quot;:6}">
    <span data-filterable-item-text="" hidden="">colors.csv</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        colors.csv
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

            <li id="file-tree-item-diff-447ae593a2fad01339a71185cf2d139a5e3aaa2007f000cca356eff4c928b09d" class="ActionList-item js-tree-node" role="treeitem" aria-level="1" style="--ActionList-tree-depth: 1;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:6,&quot;path&quot;:&quot;pic1.jpg&quot;,&quot;extension&quot;:&quot;.jpg&quot;},&quot;pull_request_id&quot;:&quot;d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;}}" data-hydro-click-hmac="5222161d0cca0f3023a3e59f88580adaa123833131d223d4b991e57a437a11cd" data-file-type=".jpg" data-file-deleted="false" data-tree-entry-type="file" data-hydro-client-context="{&quot;tree_file_count&quot;:6}">
    <span data-filterable-item-text="" hidden="">pic1.jpg</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-447ae593a2fad01339a71185cf2d139a5e3aaa2007f000cca356eff4c928b09d" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        pic1.jpg
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

            <li id="file-tree-item-diff-9c58f54e3b2ddd94f1d884d6564dbacf41f1a3e77d88ca110edc361f186657ef" class="ActionList-item js-tree-node" role="treeitem" aria-level="1" style="--ActionList-tree-depth: 1;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:6,&quot;path&quot;:&quot;pic2.jpg&quot;,&quot;extension&quot;:&quot;.jpg&quot;},&quot;pull_request_id&quot;:&quot;d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;}}" data-hydro-click-hmac="30eaa4f77f88c03b445a0b28bc84bd266700f2090b80625aa9044d773b58f670" data-file-type=".jpg" data-file-deleted="false" data-tree-entry-type="file" data-hydro-client-context="{&quot;tree_file_count&quot;:6}">
    <span data-filterable-item-text="" hidden="">pic2.jpg</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-9c58f54e3b2ddd94f1d884d6564dbacf41f1a3e77d88ca110edc361f186657ef" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        pic2.jpg
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

            <li id="file-tree-item-diff-929c963f641a0c6889cdb834f314c363d0db29991b97c835c0b18fa5b148ff95" class="ActionList-item js-tree-node" role="treeitem" aria-level="1" style="--ActionList-tree-depth: 1;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:6,&quot;path&quot;:&quot;pic3.jpg&quot;,&quot;extension&quot;:&quot;.jpg&quot;},&quot;pull_request_id&quot;:&quot;d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;}}" data-hydro-click-hmac="244f821daa7db337e8b6d2fb7cb0cea45f85435d33530000d9f221313ca4614d" data-file-type=".jpg" data-file-deleted="false" data-tree-entry-type="file" data-hydro-client-context="{&quot;tree_file_count&quot;:6}">
    <span data-filterable-item-text="" hidden="">pic3.jpg</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-929c963f641a0c6889cdb834f314c363d0db29991b97c835c0b18fa5b148ff95" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        pic3.jpg
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

      </ul>
    </nav>
  </file-tree>
</experimental-action-list>

            </div>
</div>
  <div data-target="diff-layout.mainContainer" data-view-component="true" class="Layout-main files-next-bucket">          <a name="diff-stat"></a>
          
<template class="js-comment-button-template"></template>

<div id="files" class="diff-view  js-diff-container" data-hpc="">

  <div class="container-md js-file-filter-blankslate" data-target="diff-file-filter.blankslate" hidden="">
    
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-filter blankslate-icon">
    <path d="M2.75 6a.75.75 0 0 0 0 1.5h18.5a.75.75 0 0 0 0-1.5H2.75ZM6 11.75a.75.75 0 0 1 .75-.75h10.5a.75.75 0 0 1 0 1.5H6.75a.75.75 0 0 1-.75-.75Zm4 4.938a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>

      <h2 data-view-component="true" class="blankslate-heading">        There are no files selected for viewing
</h2>
      

</div>  </div>
  </div>
  <div class="js-diff-progressive-container">
    <copilot-diff-entry data-file-path="color_detection.py">
  <div id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details open Details--on" data-file-type=".py" data-file-deleted="false" data-tagsearch-path="color_detection.py" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch" data-path="color_detection.py" data-short-path="d808305" data-anchor="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4" data-file-type=".py" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">
            69 changes: 69 additions &amp; 0 deletions
          </span>
          <span class="diffstat" aria-hidden="true">69 <span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span></span>

        
<span class="Truncate">
  <a title="color_detection.py" class="Link--primary Truncate-text" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4">color_detection.py</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="color_detection.py" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">











          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:max-content; min-width:185px; z-index:99; right: -4px;" role="menu" data-focus-trap="active"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/Bansodeprasad/Color-Detection-/blob/d2de12dff17aff39101e04671cb502efb8330376/color_detection.py" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:null,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-view-hmac="8b7f84a9b8da42b3d62d52589c220e4ecd4ebe77aae106c01740701f15b75a16">


          <div class="data highlight js-blob-wrapper">
            <template class="js-file-alert-template"></template>
<template class="js-line-alert-template"></template>



              
              <table class=" diff-table js-diff-table tab-size  " data-tab-size="8" data-diff-anchor="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4" data-paste-markdown-skip="">
                <thead class="sr-only">
                  <tr>
                      <th scope="col">Original file line number</th>
                      <th scope="col">Diff line number</th>
                      <th scope="col">Diff line change</th>
                  </tr>
                </thead>
                <tbody>
                      
      <tr data-position="0">
    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4HL0" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4HR1" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td class="blob-code blob-code-inner blob-code-hunk">@@ -0,0 +1,69 @@</td>
  </tr>

    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R1" data-line-number="1" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c"># pip install pandas opencv-python</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R2" data-line-number="2" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c"># visit pyGuru on youtube</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R3" data-line-number="3" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R4" data-line-number="4" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-k">import</span> <span class="pl-s1">cv2</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R5" data-line-number="5" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-k">import</span> <span class="pl-s1">pandas</span> <span class="pl-k">as</span> <span class="pl-s1">pd</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R6" data-line-number="6" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R7" data-line-number="7" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c"># --------------------------------------------------------------------------</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R8" data-line-number="8" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R9" data-line-number="9" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">img_path</span> <span class="pl-c1">=</span> <span class="pl-s">'pic2.jpg'</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R10" data-line-number="10" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">csv_path</span> <span class="pl-c1">=</span> <span class="pl-s">'colors.csv'</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R11" data-line-number="11" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R12" data-line-number="12" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c"># reading csv file</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R13" data-line-number="13" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">index</span> <span class="pl-c1">=</span> [<span class="pl-s">'color'</span>, <span class="pl-s">'color_name'</span>, <span class="pl-s">'hex'</span>, <span class="pl-s">'R'</span>, <span class="pl-s">'G'</span>, <span class="pl-s">'B'</span>]</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R14" data-line-number="14" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">df</span> <span class="pl-c1">=</span> <span class="pl-s1">pd</span>.<span class="pl-c1">read_csv</span>(<span class="pl-s1">csv_path</span>, <span class="pl-s1">names</span><span class="pl-c1">=</span><span class="pl-s1">index</span>, <span class="pl-s1">header</span><span class="pl-c1">=</span><span class="pl-c1">None</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R15" data-line-number="15" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R16" data-line-number="16" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c"># reading image</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R17" data-line-number="17" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">img</span> <span class="pl-c1">=</span> <span class="pl-s1">cv2</span>.<span class="pl-c1">imread</span>(<span class="pl-s1">img_path</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R18" data-line-number="18" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">img</span> <span class="pl-c1">=</span> <span class="pl-s1">cv2</span>.<span class="pl-c1">resize</span>(<span class="pl-s1">img</span>, (<span class="pl-c1">800</span>,<span class="pl-c1">600</span>))</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R19" data-line-number="19" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R20" data-line-number="20" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c">#declaring global variables</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R21" data-line-number="21" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">clicked</span> <span class="pl-c1">=</span> <span class="pl-c1">False</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R22" data-line-number="22" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">r</span> <span class="pl-c1">=</span> <span class="pl-s1">g</span> <span class="pl-c1">=</span> <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-s1">xpos</span> <span class="pl-c1">=</span> <span class="pl-s1">ypos</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R23" data-line-number="23" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R24" data-line-number="24" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c">#function to calculate minimum distance from all colors and get the most matching color</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R25" data-line-number="25" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">get_color_name</span>(<span class="pl-c1">R</span>,<span class="pl-c1">G</span>,<span class="pl-c1">B</span>):</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R26" data-line-number="26" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">	<span class="pl-s1">minimum</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R27" data-line-number="27" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">	<span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">df</span>)):</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R28" data-line-number="28" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">d</span> <span class="pl-c1">=</span> <span class="pl-en">abs</span>(<span class="pl-c1">R</span> <span class="pl-c1">-</span> <span class="pl-en">int</span>(<span class="pl-s1">df</span>.<span class="pl-c1">loc</span>[<span class="pl-s1">i</span>,<span class="pl-s">'R'</span>])) <span class="pl-c1">+</span> <span class="pl-en">abs</span>(<span class="pl-c1">G</span> <span class="pl-c1">-</span> <span class="pl-en">int</span>(<span class="pl-s1">df</span>.<span class="pl-c1">loc</span>[<span class="pl-s1">i</span>,<span class="pl-s">'G'</span>])) <span class="pl-c1">+</span> <span class="pl-en">abs</span>(<span class="pl-c1">B</span> <span class="pl-c1">-</span> <span class="pl-en">int</span>(<span class="pl-s1">df</span>.<span class="pl-c1">loc</span>[<span class="pl-s1">i</span>,<span class="pl-s">'B'</span>]))</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R29" data-line-number="29" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-k">if</span> <span class="pl-s1">d</span> <span class="pl-c1">&lt;=</span> <span class="pl-s1">minimum</span>:</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R30" data-line-number="30" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">			<span class="pl-s1">minimum</span> <span class="pl-c1">=</span> <span class="pl-s1">d</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R31" data-line-number="31" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">			<span class="pl-s1">cname</span> <span class="pl-c1">=</span> <span class="pl-s1">df</span>.<span class="pl-c1">loc</span>[<span class="pl-s1">i</span>, <span class="pl-s">'color_name'</span>]</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R32" data-line-number="32" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R33" data-line-number="33" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">	<span class="pl-k">return</span> <span class="pl-s1">cname</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R34" data-line-number="34" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R35" data-line-number="35" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c">#function to get x,y coordinates of mouse double click</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R36" data-line-number="36" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">draw_function</span>(<span class="pl-s1">event</span>, <span class="pl-s1">x</span>, <span class="pl-s1">y</span>, <span class="pl-s1">flags</span>, <span class="pl-s1">params</span>):</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R37" data-line-number="37" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">	<span class="pl-k">if</span> <span class="pl-s1">event</span> <span class="pl-c1">==</span> <span class="pl-s1">cv2</span>.<span class="pl-c1">EVENT_LBUTTONDBLCLK</span>:</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R38" data-line-number="38" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-k">global</span> <span class="pl-s1">b</span>, <span class="pl-s1">g</span>, <span class="pl-s1">r</span>, <span class="pl-s1">xpos</span>, <span class="pl-s1">ypos</span>, <span class="pl-s1">clicked</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R39" data-line-number="39" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">clicked</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R40" data-line-number="40" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">xpos</span> <span class="pl-c1">=</span> <span class="pl-s1">x</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R41" data-line-number="41" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">ypos</span> <span class="pl-c1">=</span> <span class="pl-s1">y</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R42" data-line-number="42" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">b</span>,<span class="pl-s1">g</span>,<span class="pl-s1">r</span> <span class="pl-c1">=</span> <span class="pl-s1">img</span>[<span class="pl-s1">y</span>,<span class="pl-s1">x</span>]</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R43" data-line-number="43" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-s1">b</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R44" data-line-number="44" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">g</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-s1">g</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R45" data-line-number="45" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">r</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-s1">r</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R46" data-line-number="46" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R47" data-line-number="47" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-c"># creating window</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R48" data-line-number="48" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">cv2</span>.<span class="pl-c1">namedWindow</span>(<span class="pl-s">'image'</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R49" data-line-number="49" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">cv2</span>.<span class="pl-c1">setMouseCallback</span>(<span class="pl-s">'image'</span>, <span class="pl-s1">draw_function</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R50" data-line-number="50" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R51" data-line-number="51" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-k">while</span> <span class="pl-c1">True</span>:</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R52" data-line-number="52" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">	<span class="pl-s1">cv2</span>.<span class="pl-c1">imshow</span>(<span class="pl-s">'image'</span>, <span class="pl-s1">img</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R53" data-line-number="53" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">	<span class="pl-k">if</span> <span class="pl-s1">clicked</span>:</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R54" data-line-number="54" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-c">#cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle </span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R55" data-line-number="55" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">cv2</span>.<span class="pl-c1">rectangle</span>(<span class="pl-s1">img</span>, (<span class="pl-c1">20</span>,<span class="pl-c1">20</span>), (<span class="pl-c1">600</span>,<span class="pl-c1">60</span>), (<span class="pl-s1">b</span>,<span class="pl-s1">g</span>,<span class="pl-s1">r</span>), <span class="pl-c1">-</span><span class="pl-c1">1</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R56" data-line-number="56" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R57" data-line-number="57" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-c">#Creating text string to display( Color name and RGB values )</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R58" data-line-number="58" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-en">get_color_name</span>(<span class="pl-s1">r</span>,<span class="pl-s1">g</span>,<span class="pl-s1">b</span>) <span class="pl-c1">+</span> <span class="pl-s">' R='</span> <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">r</span>) <span class="pl-c1">+</span> <span class="pl-s">' G='</span> <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">g</span>) <span class="pl-c1">+</span> <span class="pl-s">' B='</span> <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">b</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R59" data-line-number="59" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-c">#cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R60" data-line-number="60" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-s1">cv2</span>.<span class="pl-c1">putText</span>(<span class="pl-s1">img</span>, <span class="pl-s1">text</span>, (<span class="pl-c1">50</span>,<span class="pl-c1">50</span>), <span class="pl-c1">2</span>,<span class="pl-c1">0.8</span>, (<span class="pl-c1">255</span>,<span class="pl-c1">255</span>,<span class="pl-c1">255</span>),<span class="pl-c1">2</span>,<span class="pl-s1">cv2</span>.<span class="pl-c1">LINE_AA</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R61" data-line-number="61" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R62" data-line-number="62" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-c">#For very light colours we will display text in black colour</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R63" data-line-number="63" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-k">if</span> <span class="pl-s1">r</span><span class="pl-c1">+</span><span class="pl-s1">g</span><span class="pl-c1">+</span><span class="pl-s1">b</span> <span class="pl-c1">&gt;=</span><span class="pl-c1">600</span>:</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R64" data-line-number="64" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">			<span class="pl-s1">cv2</span>.<span class="pl-c1">putText</span>(<span class="pl-s1">img</span>, <span class="pl-s1">text</span>, (<span class="pl-c1">50</span>,<span class="pl-c1">50</span>), <span class="pl-c1">2</span>,<span class="pl-c1">0.8</span>, (<span class="pl-c1">0</span>,<span class="pl-c1">0</span>,<span class="pl-c1">0</span>),<span class="pl-c1">2</span>,<span class="pl-s1">cv2</span>.<span class="pl-c1">LINE_AA</span>)</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R65" data-line-number="65" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R66" data-line-number="66" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">	<span class="pl-k">if</span> <span class="pl-s1">cv2</span>.<span class="pl-c1">waitKey</span>(<span class="pl-c1">20</span>) <span class="pl-c1">&amp;</span> <span class="pl-c1">0xFF</span> <span class="pl-c1">==</span> <span class="pl-c1">27</span>:</span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R67" data-line-number="67" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">		<span class="pl-k">break</span></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R68" data-line-number="68" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="ea757ba90e6931f308fe2cfb5ceb9849ad78cffe83757ca98be38de2e0c0610e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d8083054f5c551212571bb83b7f76f52c180dcbb93cbb231c1fc284bff6761f4R69" data-line-number="69" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+"><span class="pl-s1">cv2</span>.<span class="pl-c1">destroyAllWindows</span>()</span></td>
</tr>






                </tbody>
              </table>

          </div>

    </div>
  </div>
</copilot-diff-entry>

    <copilot-diff-entry data-file-path="colorpic.jpg" data-disabled="">
  <div id="diff-d25b26e0206934607c80f8323f24c3de320a322ba8893f7d05f3bb791f9013b9" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
               display-rich-diff
              
              
              " data-file-type=".jpg" data-file-deleted="false" data-tagsearch-path="colorpic.jpg" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch" data-path="colorpic.jpg" data-short-path="d25b26e" data-anchor="diff-d25b26e0206934607c80f8323f24c3de320a322ba8893f7d05f3bb791f9013b9" data-file-type=".jpg" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">Binary file added</span>
          <span class="diffstat" aria-hidden="true">
            BIN
              <span class="color-fg-success">
                +176 KB

              </span>
          </span>

        
<span class="Truncate">
  <a title="colorpic.jpg" class="Link--primary Truncate-text" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-d25b26e0206934607c80f8323f24c3de320a322ba8893f7d05f3bb791f9013b9">colorpic.jpg</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="colorpic.jpg" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">








            <span class="BtnGroup min-width-0">
                <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-prose-diff-toggle-form" data-turbo="false" action="https://github.com/Bansodeprasad/Color-Detection-/diffs/1?commit=d2de12dff17aff39101e04671cb502efb8330376&amp;name=main&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;source=true&amp;w=false" accept-charset="UTF-8" method="get">                  <button class="btn btn-sm BtnGroup-item tooltipped tooltipped-s source js-source" aria-label="Display the source diff" type="submit" data-disable-with="">
                          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
                  </button>
</form>                  <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-prose-diff-toggle-form" data-turbo="false" action="https://github.com/Bansodeprasad/Color-Detection-/diffs/1?commit=d2de12dff17aff39101e04671cb502efb8330376&amp;name=main&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;short_path=d25b26e&amp;w=false" accept-charset="UTF-8" method="get">                    <button class="btn btn-sm BtnGroup-item tooltipped tooltipped-s rendered js-rendered selected" aria-current="true" aria-label="Display the rich diff" type="submit" data-disable-with="">
                            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file">
    <path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
                    </button>
</form>            </span>



          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:max-content; min-width:185px; z-index:99; right: -4px;" role="menu">
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/Bansodeprasad/Color-Detection-/blob/d2de12dff17aff39101e04671cb502efb8330376/colorpic.jpg" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            </details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:null,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-view-hmac="8b7f84a9b8da42b3d62d52589c220e4ecd4ebe77aae106c01740701f15b75a16">
            <div class="render-wrapper ">
    <div class="render-container js-render-target is-render-automatic is-render-requested is-render-ready" data-identity="f1926ddf-e58f-4fe4-afa4-f4912350ffc1" data-host="https://viewscreen.githubusercontent.com" data-type="img" style="height: 457.2px;">
      <span data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="64" height="64" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="octospinner mx-auto anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
      <div class="render-viewer-error">Sorry, something went wrong. <a class="Link--inTextBlock" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376">Reload?</a></div>
      <div class="render-viewer-fatal">Sorry, we cannot display this file.</div>
      <div class="render-viewer-invalid">Sorry, this file is invalid so it cannot be displayed.</div>
      <iframe class="render-viewer " src="./color_detection_files/img.html" sandbox="allow-scripts allow-same-origin allow-top-navigation" title="File display" name="f1926ddf-e58f-4fe4-afa4-f4912350ffc1">
          Viewer requires iframe.
      </iframe>
    </div>
  </div>
 

    </div>
  </div>
</copilot-diff-entry>

  </div>

    <div class="js-diff-progressive-container">
    <copilot-diff-entry data-file-path="colors.csv">
  <div id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details Details--on open" data-file-type=".csv" data-file-deleted="false" data-tagsearch-path="colors.csv" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch" data-path="colors.csv" data-short-path="d3dd53c" data-anchor="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604" data-file-type=".csv" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">
            865 changes: 865 additions &amp; 0 deletions
          </span>
          <span class="diffstat" aria-hidden="true">865 <span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span></span>

        
<span class="Truncate">
  <a title="colors.csv" class="Link--primary Truncate-text" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604">colors.csv</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="colors.csv" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">











          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:max-content; min-width:185px; z-index:99; right: -4px;" role="menu">
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/Bansodeprasad/Color-Detection-/blob/d2de12dff17aff39101e04671cb502efb8330376/colors.csv" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            </details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:null,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/diffs?bytes=2054&amp;commit=d2de12dff17aff39101e04671cb502efb8330376&amp;lines=70&amp;responsive=true&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;start_entry=2&amp;sticky=false&amp;w=false&quot;,&quot;user_id&quot;:null}}" data-hydro-view-hmac="da27f168452f5401cc39365cfa7bab7808b0055f832c759ca5c44e87de6005c1">
            <div class="js-diff-load-container" tabindex="-1">
  

          <div class="data highlight js-blob-wrapper">
            <template class="js-file-alert-template"></template>
<template class="js-line-alert-template"></template>



              
              <table class=" diff-table js-diff-table tab-size  " data-tab-size="8" data-diff-anchor="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604" data-paste-markdown-skip="">
                <thead class="sr-only">
                  <tr>
                      <th scope="col">Original file line number</th>
                      <th scope="col">Diff line number</th>
                      <th scope="col">Diff line change</th>
                  </tr>
                </thead>
                <tbody>
                      
      <tr data-position="0">
    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604HL0" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604HR1" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td class="blob-code blob-code-inner blob-code-hunk">@@ -0,0 +1,865 @@</td>
  </tr>

    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R1" data-line-number="1" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">air_force_blue_raf,"Air Force Blue (Raf)",#5d8aa8,93,138,168</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R2" data-line-number="2" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">air_force_blue_usaf,"Air Force Blue (Usaf)",#00308f,0,48,143</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R3" data-line-number="3" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">air_superiority_blue,"Air Superiority Blue",#72a0c1,114,160,193</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R4" data-line-number="4" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">alabama_crimson,"Alabama Crimson",#a32638,163,38,56</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R5" data-line-number="5" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">alice_blue,"Alice Blue",#f0f8ff,240,248,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R6" data-line-number="6" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">alizarin_crimson,"Alizarin Crimson",#e32636,227,38,54</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R7" data-line-number="7" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">alloy_orange,"Alloy Orange",#c46210,196,98,16</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R8" data-line-number="8" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">almond,"Almond",#efdecd,239,222,205</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R9" data-line-number="9" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">amaranth,"Amaranth",#e52b50,229,43,80</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R10" data-line-number="10" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">amber,"Amber",#ffbf00,255,191,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R11" data-line-number="11" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">amber_sae_ece,"Amber (Sae/Ece)",#ff7e00,255,126,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R12" data-line-number="12" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">american_rose,"American Rose",#ff033e,255,3,62</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R13" data-line-number="13" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">amethyst,"Amethyst",#96c,153,102,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R14" data-line-number="14" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">android_green,"Android Green",#a4c639,164,198,57</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R15" data-line-number="15" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">anti_flash_white,"Anti-Flash White",#f2f3f4,242,243,244</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R16" data-line-number="16" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">antique_brass,"Antique Brass",#cd9575,205,149,117</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R17" data-line-number="17" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">antique_fuchsia,"Antique Fuchsia",#915c83,145,92,131</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R18" data-line-number="18" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">antique_ruby,"Antique Ruby",#841b2d,132,27,45</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R19" data-line-number="19" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">antique_white,"Antique White",#faebd7,250,235,215</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R20" data-line-number="20" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ao_english,"Ao (English)",#008000,0,128,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R21" data-line-number="21" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">apple_green,"Apple Green",#8db600,141,182,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R22" data-line-number="22" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">apricot,"Apricot",#fbceb1,251,206,177</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R23" data-line-number="23" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">aqua,"Aqua",#0ff,0,255,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R24" data-line-number="24" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">aquamarine,"Aquamarine",#7fffd4,127,255,212</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R25" data-line-number="25" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">army_green,"Army Green",#4b5320,75,83,32</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R26" data-line-number="26" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">arsenic,"Arsenic",#3b444b,59,68,75</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R27" data-line-number="27" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">arylide_yellow,"Arylide Yellow",#e9d66b,233,214,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R28" data-line-number="28" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ash_grey,"Ash Grey",#b2beb5,178,190,181</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R29" data-line-number="29" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">asparagus,"Asparagus",#87a96b,135,169,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R30" data-line-number="30" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">atomic_tangerine,"Atomic Tangerine",#f96,255,153,102</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R31" data-line-number="31" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">auburn,"Auburn",#a52a2a,165,42,42</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R32" data-line-number="32" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">aureolin,"Aureolin",#fdee00,253,238,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R33" data-line-number="33" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">aurometalsaurus,"Aurometalsaurus",#6e7f80,110,127,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R34" data-line-number="34" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">avocado,"Avocado",#568203,86,130,3</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R35" data-line-number="35" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">azure,"Azure",#007fff,0,127,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R36" data-line-number="36" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">azure_mist_web,"Azure Mist/Web",#f0ffff,240,255,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R37" data-line-number="37" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">baby_blue,"Baby Blue",#89cff0,137,207,240</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R38" data-line-number="38" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">baby_blue_eyes,"Baby Blue Eyes",#a1caf1,161,202,241</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R39" data-line-number="39" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">baby_pink,"Baby Pink",#f4c2c2,244,194,194</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R40" data-line-number="40" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ball_blue,"Ball Blue",#21abcd,33,171,205</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R41" data-line-number="41" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">banana_mania,"Banana Mania",#fae7b5,250,231,181</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R42" data-line-number="42" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">banana_yellow,"Banana Yellow",#ffe135,255,225,53</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R43" data-line-number="43" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">barn_red,"Barn Red",#7c0a02,124,10,2</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R44" data-line-number="44" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">battleship_grey,"Battleship Grey",#848482,132,132,130</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R45" data-line-number="45" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bazaar,"Bazaar",#98777b,152,119,123</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R46" data-line-number="46" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">beau_blue,"Beau Blue",#bcd4e6,188,212,230</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R47" data-line-number="47" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">beaver,"Beaver",#9f8170,159,129,112</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R48" data-line-number="48" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">beige,"Beige",#f5f5dc,245,245,220</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R49" data-line-number="49" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">big_dip_o_ruby,"Big Dip O’Ruby",#9c2542,156,37,66</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R50" data-line-number="50" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bisque,"Bisque",#ffe4c4,255,228,196</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R51" data-line-number="51" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bistre,"Bistre",#3d2b1f,61,43,31</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R52" data-line-number="52" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bittersweet,"Bittersweet",#fe6f5e,254,111,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R53" data-line-number="53" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bittersweet_shimmer,"Bittersweet Shimmer",#bf4f51,191,79,81</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R54" data-line-number="54" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">black,"Black",#000,0,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R55" data-line-number="55" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">black_bean,"Black Bean",#3d0c02,61,12,2</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R56" data-line-number="56" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">black_leather_jacket,"Black Leather Jacket",#253529,37,53,41</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R57" data-line-number="57" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">black_olive,"Black Olive",#3b3c36,59,60,54</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R58" data-line-number="58" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blanched_almond,"Blanched Almond",#ffebcd,255,235,205</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R59" data-line-number="59" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blast_off_bronze,"Blast-Off Bronze",#a57164,165,113,100</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R60" data-line-number="60" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bleu_de_france,"Bleu De France",#318ce7,49,140,231</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R61" data-line-number="61" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blizzard_blue,"Blizzard Blue",#ace5ee,172,229,238</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R62" data-line-number="62" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blond,"Blond",#faf0be,250,240,190</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R63" data-line-number="63" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue,"Blue",#00f,0,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R64" data-line-number="64" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_bell,"Blue Bell",#a2a2d0,162,162,208</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R65" data-line-number="65" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_crayola,"Blue (Crayola)",#1f75fe,31,117,254</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R66" data-line-number="66" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_gray,"Blue Gray",#69c,102,153,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R67" data-line-number="67" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_green,"Blue-Green",#0d98ba,13,152,186</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R68" data-line-number="68" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_munsell,"Blue (Munsell)",#0093af,0,147,175</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R69" data-line-number="69" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_ncs,"Blue (Ncs)",#0087bd,0,135,189</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R70" data-line-number="70" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_pigment,"Blue (Pigment)",#339,51,51,153</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R71" data-line-number="71" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_ryb,"Blue (Ryb)",#0247fe,2,71,254</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R72" data-line-number="72" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_sapphire,"Blue Sapphire",#126180,18,97,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R73" data-line-number="73" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blue_violet,"Blue-Violet",#8a2be2,138,43,226</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R74" data-line-number="74" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">blush,"Blush",#de5d83,222,93,131</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R75" data-line-number="75" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bole,"Bole",#79443b,121,68,59</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R76" data-line-number="76" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bondi_blue,"Bondi Blue",#0095b6,0,149,182</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R77" data-line-number="77" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bone,"Bone",#e3dac9,227,218,201</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R78" data-line-number="78" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">boston_university_red,"Boston University Red",#c00,204,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R79" data-line-number="79" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bottle_green,"Bottle Green",#006a4e,0,106,78</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R80" data-line-number="80" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">boysenberry,"Boysenberry",#873260,135,50,96</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R81" data-line-number="81" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">brandeis_blue,"Brandeis Blue",#0070ff,0,112,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R82" data-line-number="82" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">brass,"Brass",#b5a642,181,166,66</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R83" data-line-number="83" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">brick_red,"Brick Red",#cb4154,203,65,84</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R84" data-line-number="84" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bright_cerulean,"Bright Cerulean",#1dacd6,29,172,214</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R85" data-line-number="85" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bright_green,"Bright Green",#6f0,102,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R86" data-line-number="86" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bright_lavender,"Bright Lavender",#bf94e4,191,148,228</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R87" data-line-number="87" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bright_maroon,"Bright Maroon",#c32148,195,33,72</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R88" data-line-number="88" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bright_pink,"Bright Pink",#ff007f,255,0,127</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R89" data-line-number="89" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bright_turquoise,"Bright Turquoise",#08e8de,8,232,222</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R90" data-line-number="90" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bright_ube,"Bright Ube",#d19fe8,209,159,232</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R91" data-line-number="91" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">brilliant_lavender,"Brilliant Lavender",#f4bbff,244,187,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R92" data-line-number="92" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">brilliant_rose,"Brilliant Rose",#ff55a3,255,85,163</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R93" data-line-number="93" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">brink_pink,"Brink Pink",#fb607f,251,96,127</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R94" data-line-number="94" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">british_racing_green,"British Racing Green",#004225,0,66,37</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R95" data-line-number="95" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bronze,"Bronze",#cd7f32,205,127,50</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R96" data-line-number="96" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">brown_traditional,"Brown (Traditional)",#964b00,150,75,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R97" data-line-number="97" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">brown_web,"Brown (Web)",#a52a2a,165,42,42</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R98" data-line-number="98" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bubble_gum,"Bubble Gum",#ffc1cc,255,193,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R99" data-line-number="99" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bubbles,"Bubbles",#e7feff,231,254,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R100" data-line-number="100" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">buff,"Buff",#f0dc82,240,220,130</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R101" data-line-number="101" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">bulgarian_rose,"Bulgarian Rose",#480607,72,6,7</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R102" data-line-number="102" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">burgundy,"Burgundy",#800020,128,0,32</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R103" data-line-number="103" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">burlywood,"Burlywood",#deb887,222,184,135</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R104" data-line-number="104" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">burnt_orange,"Burnt Orange",#c50,204,85,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R105" data-line-number="105" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">burnt_sienna,"Burnt Sienna",#e97451,233,116,81</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R106" data-line-number="106" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">burnt_umber,"Burnt Umber",#8a3324,138,51,36</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R107" data-line-number="107" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">byzantine,"Byzantine",#bd33a4,189,51,164</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R108" data-line-number="108" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">byzantium,"Byzantium",#702963,112,41,99</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R109" data-line-number="109" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cadet,"Cadet",#536872,83,104,114</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R110" data-line-number="110" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cadet_blue,"Cadet Blue",#5f9ea0,95,158,160</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R111" data-line-number="111" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cadet_grey,"Cadet Grey",#91a3b0,145,163,176</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R112" data-line-number="112" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cadmium_green,"Cadmium Green",#006b3c,0,107,60</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R113" data-line-number="113" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cadmium_orange,"Cadmium Orange",#ed872d,237,135,45</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R114" data-line-number="114" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cadmium_red,"Cadmium Red",#e30022,227,0,34</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R115" data-line-number="115" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cadmium_yellow,"Cadmium Yellow",#fff600,255,246,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R116" data-line-number="116" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">caf_au_lait,"Café Au Lait",#a67b5b,166,123,91</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R117" data-line-number="117" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">caf_noir,"Café Noir",#4b3621,75,54,33</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R118" data-line-number="118" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cal_poly_green,"Cal Poly Green",#1e4d2b,30,77,43</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R119" data-line-number="119" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cambridge_blue,"Cambridge Blue",#a3c1ad,163,193,173</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R120" data-line-number="120" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">camel,"Camel",#c19a6b,193,154,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R121" data-line-number="121" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cameo_pink,"Cameo Pink",#efbbcc,239,187,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R122" data-line-number="122" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">camouflage_green,"Camouflage Green",#78866b,120,134,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R123" data-line-number="123" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">canary_yellow,"Canary Yellow",#ffef00,255,239,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R124" data-line-number="124" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">candy_apple_red,"Candy Apple Red",#ff0800,255,8,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R125" data-line-number="125" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">candy_pink,"Candy Pink",#e4717a,228,113,122</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R126" data-line-number="126" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">capri,"Capri",#00bfff,0,191,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R127" data-line-number="127" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">caput_mortuum,"Caput Mortuum",#592720,89,39,32</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R128" data-line-number="128" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cardinal,"Cardinal",#c41e3a,196,30,58</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R129" data-line-number="129" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">caribbean_green,"Caribbean Green",#0c9,0,204,153</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R130" data-line-number="130" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">carmine,"Carmine",#960018,150,0,24</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R131" data-line-number="131" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">carmine_m_p,"Carmine (M&amp;P)",#d70040,215,0,64</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R132" data-line-number="132" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">carmine_pink,"Carmine Pink",#eb4c42,235,76,66</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R133" data-line-number="133" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">carmine_red,"Carmine Red",#ff0038,255,0,56</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R134" data-line-number="134" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">carnation_pink,"Carnation Pink",#ffa6c9,255,166,201</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R135" data-line-number="135" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">carnelian,"Carnelian",#b31b1b,179,27,27</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R136" data-line-number="136" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">carolina_blue,"Carolina Blue",#99badd,153,186,221</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R137" data-line-number="137" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">carrot_orange,"Carrot Orange",#ed9121,237,145,33</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R138" data-line-number="138" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">catalina_blue,"Catalina Blue",#062a78,6,42,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R139" data-line-number="139" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ceil,"Ceil",#92a1cf,146,161,207</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R140" data-line-number="140" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">celadon,"Celadon",#ace1af,172,225,175</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R141" data-line-number="141" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">celadon_blue,"Celadon Blue",#007ba7,0,123,167</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R142" data-line-number="142" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">celadon_green,"Celadon Green",#2f847c,47,132,124</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R143" data-line-number="143" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">celeste_colour,"Celeste (Colour)",#b2ffff,178,255,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R144" data-line-number="144" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">celestial_blue,"Celestial Blue",#4997d0,73,151,208</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R145" data-line-number="145" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cerise,"Cerise",#de3163,222,49,99</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R146" data-line-number="146" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cerise_pink,"Cerise Pink",#ec3b83,236,59,131</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R147" data-line-number="147" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cerulean,"Cerulean",#007ba7,0,123,167</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R148" data-line-number="148" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cerulean_blue,"Cerulean Blue",#2a52be,42,82,190</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R149" data-line-number="149" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cerulean_frost,"Cerulean Frost",#6d9bc3,109,155,195</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R150" data-line-number="150" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cg_blue,"Cg Blue",#007aa5,0,122,165</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R151" data-line-number="151" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cg_red,"Cg Red",#e03c31,224,60,49</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R152" data-line-number="152" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">chamoisee,"Chamoisee",#a0785a,160,120,90</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R153" data-line-number="153" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">champagne,"Champagne",#fad6a5,250,214,165</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R154" data-line-number="154" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">charcoal,"Charcoal",#36454f,54,69,79</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R155" data-line-number="155" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">charm_pink,"Charm Pink",#e68fac,230,143,172</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R156" data-line-number="156" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">chartreuse_traditional,"Chartreuse (Traditional)",#dfff00,223,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R157" data-line-number="157" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">chartreuse_web,"Chartreuse (Web)",#7fff00,127,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R158" data-line-number="158" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cherry,"Cherry",#de3163,222,49,99</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R159" data-line-number="159" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cherry_blossom_pink,"Cherry Blossom Pink",#ffb7c5,255,183,197</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R160" data-line-number="160" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">chestnut,"Chestnut",#cd5c5c,205,92,92</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R161" data-line-number="161" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">china_pink,"China Pink",#de6fa1,222,111,161</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R162" data-line-number="162" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">china_rose,"China Rose",#a8516e,168,81,110</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R163" data-line-number="163" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">chinese_red,"Chinese Red",#aa381e,170,56,30</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R164" data-line-number="164" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">chocolate_traditional,"Chocolate (Traditional)",#7b3f00,123,63,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R165" data-line-number="165" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">chocolate_web,"Chocolate (Web)",#d2691e,210,105,30</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R166" data-line-number="166" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">chrome_yellow,"Chrome Yellow",#ffa700,255,167,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R167" data-line-number="167" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cinereous,"Cinereous",#98817b,152,129,123</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R168" data-line-number="168" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cinnabar,"Cinnabar",#e34234,227,66,52</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R169" data-line-number="169" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cinnamon,"Cinnamon",#d2691e,210,105,30</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R170" data-line-number="170" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">citrine,"Citrine",#e4d00a,228,208,10</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R171" data-line-number="171" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">classic_rose,"Classic Rose",#fbcce7,251,204,231</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R172" data-line-number="172" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cobalt,"Cobalt",#0047ab,0,71,171</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R173" data-line-number="173" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cocoa_brown,"Cocoa Brown",#d2691e,210,105,30</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R174" data-line-number="174" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">coffee,"Coffee",#6f4e37,111,78,55</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R175" data-line-number="175" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">columbia_blue,"Columbia Blue",#9bddff,155,221,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R176" data-line-number="176" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">congo_pink,"Congo Pink",#f88379,248,131,121</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R177" data-line-number="177" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cool_black,"Cool Black",#002e63,0,46,99</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R178" data-line-number="178" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cool_grey,"Cool Grey",#8c92ac,140,146,172</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R179" data-line-number="179" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">copper,"Copper",#b87333,184,115,51</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R180" data-line-number="180" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">copper_crayola,"Copper (Crayola)",#da8a67,218,138,103</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R181" data-line-number="181" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">copper_penny,"Copper Penny",#ad6f69,173,111,105</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R182" data-line-number="182" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">copper_red,"Copper Red",#cb6d51,203,109,81</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R183" data-line-number="183" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">copper_rose,"Copper Rose",#966,153,102,102</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R184" data-line-number="184" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">coquelicot,"Coquelicot",#ff3800,255,56,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R185" data-line-number="185" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">coral,"Coral",#ff7f50,255,127,80</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R186" data-line-number="186" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">coral_pink,"Coral Pink",#f88379,248,131,121</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R187" data-line-number="187" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">coral_red,"Coral Red",#ff4040,255,64,64</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R188" data-line-number="188" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cordovan,"Cordovan",#893f45,137,63,69</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R189" data-line-number="189" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">corn,"Corn",#fbec5d,251,236,93</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R190" data-line-number="190" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cornell_red,"Cornell Red",#b31b1b,179,27,27</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R191" data-line-number="191" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cornflower_blue,"Cornflower Blue",#6495ed,100,149,237</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R192" data-line-number="192" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cornsilk,"Cornsilk",#fff8dc,255,248,220</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R193" data-line-number="193" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cosmic_latte,"Cosmic Latte",#fff8e7,255,248,231</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R194" data-line-number="194" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cotton_candy,"Cotton Candy",#ffbcd9,255,188,217</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R195" data-line-number="195" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cream,"Cream",#fffdd0,255,253,208</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R196" data-line-number="196" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">crimson,"Crimson",#dc143c,220,20,60</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R197" data-line-number="197" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">crimson_glory,"Crimson Glory",#be0032,190,0,50</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R198" data-line-number="198" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cyan,"Cyan",#0ff,0,255,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R199" data-line-number="199" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">cyan_process,"Cyan (Process)",#00b7eb,0,183,235</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R200" data-line-number="200" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">daffodil,"Daffodil",#ffff31,255,255,49</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R201" data-line-number="201" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dandelion,"Dandelion",#f0e130,240,225,48</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R202" data-line-number="202" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_blue,"Dark Blue",#00008b,0,0,139</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R203" data-line-number="203" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_brown,"Dark Brown",#654321,101,67,33</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R204" data-line-number="204" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_byzantium,"Dark Byzantium",#5d3954,93,57,84</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R205" data-line-number="205" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_candy_apple_red,"Dark Candy Apple Red",#a40000,164,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R206" data-line-number="206" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_cerulean,"Dark Cerulean",#08457e,8,69,126</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R207" data-line-number="207" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_chestnut,"Dark Chestnut",#986960,152,105,96</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R208" data-line-number="208" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_coral,"Dark Coral",#cd5b45,205,91,69</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R209" data-line-number="209" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_cyan,"Dark Cyan",#008b8b,0,139,139</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R210" data-line-number="210" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_electric_blue,"Dark Electric Blue",#536878,83,104,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R211" data-line-number="211" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_goldenrod,"Dark Goldenrod",#b8860b,184,134,11</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R212" data-line-number="212" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_gray,"Dark Gray",#a9a9a9,169,169,169</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R213" data-line-number="213" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_green,"Dark Green",#013220,1,50,32</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R214" data-line-number="214" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_imperial_blue,"Dark Imperial Blue",#00416a,0,65,106</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R215" data-line-number="215" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_jungle_green,"Dark Jungle Green",#1a2421,26,36,33</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R216" data-line-number="216" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_khaki,"Dark Khaki",#bdb76b,189,183,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R217" data-line-number="217" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_lava,"Dark Lava",#483c32,72,60,50</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R218" data-line-number="218" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_lavender,"Dark Lavender",#734f96,115,79,150</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R219" data-line-number="219" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_magenta,"Dark Magenta",#8b008b,139,0,139</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R220" data-line-number="220" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_midnight_blue,"Dark Midnight Blue",#036,0,51,102</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R221" data-line-number="221" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_olive_green,"Dark Olive Green",#556b2f,85,107,47</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R222" data-line-number="222" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_orange,"Dark Orange",#ff8c00,255,140,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R223" data-line-number="223" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_orchid,"Dark Orchid",#9932cc,153,50,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R224" data-line-number="224" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_pastel_blue,"Dark Pastel Blue",#779ecb,119,158,203</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R225" data-line-number="225" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_pastel_green,"Dark Pastel Green",#03c03c,3,192,60</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R226" data-line-number="226" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_pastel_purple,"Dark Pastel Purple",#966fd6,150,111,214</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R227" data-line-number="227" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_pastel_red,"Dark Pastel Red",#c23b22,194,59,34</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R228" data-line-number="228" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_pink,"Dark Pink",#e75480,231,84,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R229" data-line-number="229" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_powder_blue,"Dark Powder Blue",#039,0,51,153</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R230" data-line-number="230" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_raspberry,"Dark Raspberry",#872657,135,38,87</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R231" data-line-number="231" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_red,"Dark Red",#8b0000,139,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R232" data-line-number="232" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_salmon,"Dark Salmon",#e9967a,233,150,122</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R233" data-line-number="233" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_scarlet,"Dark Scarlet",#560319,86,3,25</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R234" data-line-number="234" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_sea_green,"Dark Sea Green",#8fbc8f,143,188,143</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R235" data-line-number="235" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_sienna,"Dark Sienna",#3c1414,60,20,20</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R236" data-line-number="236" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_slate_blue,"Dark Slate Blue",#483d8b,72,61,139</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R237" data-line-number="237" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_slate_gray,"Dark Slate Gray",#2f4f4f,47,79,79</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R238" data-line-number="238" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_spring_green,"Dark Spring Green",#177245,23,114,69</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R239" data-line-number="239" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_tan,"Dark Tan",#918151,145,129,81</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R240" data-line-number="240" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_tangerine,"Dark Tangerine",#ffa812,255,168,18</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R241" data-line-number="241" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_taupe,"Dark Taupe",#483c32,72,60,50</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R242" data-line-number="242" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_terra_cotta,"Dark Terra Cotta",#cc4e5c,204,78,92</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R243" data-line-number="243" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_turquoise,"Dark Turquoise",#00ced1,0,206,209</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R244" data-line-number="244" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_violet,"Dark Violet",#9400d3,148,0,211</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R245" data-line-number="245" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dark_yellow,"Dark Yellow",#9b870c,155,135,12</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R246" data-line-number="246" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dartmouth_green,"Dartmouth Green",#00703c,0,112,60</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R247" data-line-number="247" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">davy_s_grey,"Davy'S Grey",#555,85,85,85</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R248" data-line-number="248" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">debian_red,"Debian Red",#d70a53,215,10,83</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R249" data-line-number="249" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_carmine,"Deep Carmine",#a9203e,169,32,62</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R250" data-line-number="250" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_carmine_pink,"Deep Carmine Pink",#ef3038,239,48,56</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R251" data-line-number="251" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_carrot_orange,"Deep Carrot Orange",#e9692c,233,105,44</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R252" data-line-number="252" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_cerise,"Deep Cerise",#da3287,218,50,135</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R253" data-line-number="253" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_champagne,"Deep Champagne",#fad6a5,250,214,165</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R254" data-line-number="254" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_chestnut,"Deep Chestnut",#b94e48,185,78,72</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R255" data-line-number="255" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_coffee,"Deep Coffee",#704241,112,66,65</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R256" data-line-number="256" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_fuchsia,"Deep Fuchsia",#c154c1,193,84,193</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R257" data-line-number="257" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_jungle_green,"Deep Jungle Green",#004b49,0,75,73</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R258" data-line-number="258" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_lilac,"Deep Lilac",#95b,153,85,187</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R259" data-line-number="259" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_magenta,"Deep Magenta",#c0c,204,0,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R260" data-line-number="260" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_peach,"Deep Peach",#ffcba4,255,203,164</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R261" data-line-number="261" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_pink,"Deep Pink",#ff1493,255,20,147</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R262" data-line-number="262" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_ruby,"Deep Ruby",#843f5b,132,63,91</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R263" data-line-number="263" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_saffron,"Deep Saffron",#f93,255,153,51</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R264" data-line-number="264" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_sky_blue,"Deep Sky Blue",#00bfff,0,191,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R265" data-line-number="265" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">deep_tuscan_red,"Deep Tuscan Red",#66424d,102,66,77</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R266" data-line-number="266" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">denim,"Denim",#1560bd,21,96,189</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R267" data-line-number="267" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">desert,"Desert",#c19a6b,193,154,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R268" data-line-number="268" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">desert_sand,"Desert Sand",#edc9af,237,201,175</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R269" data-line-number="269" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dim_gray,"Dim Gray",#696969,105,105,105</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R270" data-line-number="270" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dodger_blue,"Dodger Blue",#1e90ff,30,144,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R271" data-line-number="271" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dogwood_rose,"Dogwood Rose",#d71868,215,24,104</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R272" data-line-number="272" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">dollar_bill,"Dollar Bill",#85bb65,133,187,101</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R273" data-line-number="273" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">drab,"Drab",#967117,150,113,23</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R274" data-line-number="274" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">duke_blue,"Duke Blue",#00009c,0,0,156</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R275" data-line-number="275" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">earth_yellow,"Earth Yellow",#e1a95f,225,169,95</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R276" data-line-number="276" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ebony,"Ebony",#555d50,85,93,80</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R277" data-line-number="277" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ecru,"Ecru",#c2b280,194,178,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R278" data-line-number="278" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">eggplant,"Eggplant",#614051,97,64,81</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R279" data-line-number="279" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">eggshell,"Eggshell",#f0ead6,240,234,214</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R280" data-line-number="280" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">egyptian_blue,"Egyptian Blue",#1034a6,16,52,166</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R281" data-line-number="281" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_blue,"Electric Blue",#7df9ff,125,249,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R282" data-line-number="282" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_crimson,"Electric Crimson",#ff003f,255,0,63</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R283" data-line-number="283" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_cyan,"Electric Cyan",#0ff,0,255,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R284" data-line-number="284" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_green,"Electric Green",#0f0,0,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R285" data-line-number="285" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_indigo,"Electric Indigo",#6f00ff,111,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R286" data-line-number="286" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_lavender,"Electric Lavender",#f4bbff,244,187,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R287" data-line-number="287" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_lime,"Electric Lime",#cf0,204,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R288" data-line-number="288" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_purple,"Electric Purple",#bf00ff,191,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R289" data-line-number="289" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_ultramarine,"Electric Ultramarine",#3f00ff,63,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R290" data-line-number="290" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_violet,"Electric Violet",#8f00ff,143,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R291" data-line-number="291" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">electric_yellow,"Electric Yellow",#ff0,255,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R292" data-line-number="292" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">emerald,"Emerald",#50c878,80,200,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R293" data-line-number="293" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">english_lavender,"English Lavender",#b48395,180,131,149</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R294" data-line-number="294" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">eton_blue,"Eton Blue",#96c8a2,150,200,162</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R295" data-line-number="295" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fallow,"Fallow",#c19a6b,193,154,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R296" data-line-number="296" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">falu_red,"Falu Red",#801818,128,24,24</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R297" data-line-number="297" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fandango,"Fandango",#b53389,181,51,137</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R298" data-line-number="298" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fashion_fuchsia,"Fashion Fuchsia",#f400a1,244,0,161</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R299" data-line-number="299" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fawn,"Fawn",#e5aa70,229,170,112</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R300" data-line-number="300" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">feldgrau,"Feldgrau",#4d5d53,77,93,83</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R301" data-line-number="301" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fern_green,"Fern Green",#4f7942,79,121,66</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R302" data-line-number="302" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ferrari_red,"Ferrari Red",#ff2800,255,40,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R303" data-line-number="303" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">field_drab,"Field Drab",#6c541e,108,84,30</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R304" data-line-number="304" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fire_engine_red,"Fire Engine Red",#ce2029,206,32,41</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R305" data-line-number="305" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">firebrick,"Firebrick",#b22222,178,34,34</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R306" data-line-number="306" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">flame,"Flame",#e25822,226,88,34</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R307" data-line-number="307" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">flamingo_pink,"Flamingo Pink",#fc8eac,252,142,172</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R308" data-line-number="308" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">flavescent,"Flavescent",#f7e98e,247,233,142</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R309" data-line-number="309" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">flax,"Flax",#eedc82,238,220,130</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R310" data-line-number="310" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">floral_white,"Floral White",#fffaf0,255,250,240</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R311" data-line-number="311" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fluorescent_orange,"Fluorescent Orange",#ffbf00,255,191,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R312" data-line-number="312" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fluorescent_pink,"Fluorescent Pink",#ff1493,255,20,147</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R313" data-line-number="313" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fluorescent_yellow,"Fluorescent Yellow",#cf0,204,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R314" data-line-number="314" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">folly,"Folly",#ff004f,255,0,79</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R315" data-line-number="315" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">forest_green_traditional,"Forest Green (Traditional)",#014421,1,68,33</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R316" data-line-number="316" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">forest_green_web,"Forest Green (Web)",#228b22,34,139,34</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R317" data-line-number="317" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">french_beige,"French Beige",#a67b5b,166,123,91</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R318" data-line-number="318" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">french_blue,"French Blue",#0072bb,0,114,187</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R319" data-line-number="319" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">french_lilac,"French Lilac",#86608e,134,96,142</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R320" data-line-number="320" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">french_lime,"French Lime",#cf0,204,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R321" data-line-number="321" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">french_raspberry,"French Raspberry",#c72c48,199,44,72</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R322" data-line-number="322" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">french_rose,"French Rose",#f64a8a,246,74,138</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R323" data-line-number="323" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fuchsia,"Fuchsia",#f0f,255,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R324" data-line-number="324" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fuchsia_crayola,"Fuchsia (Crayola)",#c154c1,193,84,193</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R325" data-line-number="325" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fuchsia_pink,"Fuchsia Pink",#f7f,255,119,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R326" data-line-number="326" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fuchsia_rose,"Fuchsia Rose",#c74375,199,67,117</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R327" data-line-number="327" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fulvous,"Fulvous",#e48400,228,132,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R328" data-line-number="328" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">fuzzy_wuzzy,"Fuzzy Wuzzy",#c66,204,102,102</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R329" data-line-number="329" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">gainsboro,"Gainsboro",#dcdcdc,220,220,220</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R330" data-line-number="330" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">gamboge,"Gamboge",#e49b0f,228,155,15</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R331" data-line-number="331" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ghost_white,"Ghost White",#f8f8ff,248,248,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R332" data-line-number="332" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ginger,"Ginger",#b06500,176,101,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R333" data-line-number="333" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">glaucous,"Glaucous",#6082b6,96,130,182</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R334" data-line-number="334" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">glitter,"Glitter",#e6e8fa,230,232,250</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R335" data-line-number="335" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">gold_metallic,"Gold (Metallic)",#d4af37,212,175,55</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R336" data-line-number="336" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">gold_web_golden,"Gold (Web) (Golden)",#ffd700,255,215,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R337" data-line-number="337" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">golden_brown,"Golden Brown",#996515,153,101,21</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R338" data-line-number="338" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">golden_poppy,"Golden Poppy",#fcc200,252,194,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R339" data-line-number="339" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">golden_yellow,"Golden Yellow",#ffdf00,255,223,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R340" data-line-number="340" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">goldenrod,"Goldenrod",#daa520,218,165,32</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R341" data-line-number="341" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">granny_smith_apple,"Granny Smith Apple",#a8e4a0,168,228,160</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R342" data-line-number="342" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">gray,"Gray",#808080,128,128,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R343" data-line-number="343" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">gray_asparagus,"Gray-Asparagus",#465945,70,89,69</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R344" data-line-number="344" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">gray_html_css_gray,"Gray (Html/Css Gray)",#808080,128,128,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R345" data-line-number="345" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">gray_x11_gray,"Gray (X11 Gray)",#bebebe,190,190,190</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R346" data-line-number="346" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">green_color_wheel_x11_green,"Green (Color Wheel) (X11 Green)",#0f0,0,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R347" data-line-number="347" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">green_crayola,"Green (Crayola)",#1cac78,28,172,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R348" data-line-number="348" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">green_html_css_green,"Green (Html/Css Green)",#008000,0,128,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R349" data-line-number="349" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">green_munsell,"Green (Munsell)",#00a877,0,168,119</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R350" data-line-number="350" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">green_ncs,"Green (Ncs)",#009f6b,0,159,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R351" data-line-number="351" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">green_pigment,"Green (Pigment)",#00a550,0,165,80</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R352" data-line-number="352" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">green_ryb,"Green (Ryb)",#66b032,102,176,50</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R353" data-line-number="353" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">green_yellow,"Green-Yellow",#adff2f,173,255,47</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R354" data-line-number="354" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">grullo,"Grullo",#a99a86,169,154,134</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R355" data-line-number="355" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">guppie_green,"Guppie Green",#00ff7f,0,255,127</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R356" data-line-number="356" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">halay_be,"Halayà úBe",#663854,102,56,84</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R357" data-line-number="357" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">han_blue,"Han Blue",#446ccf,68,108,207</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R358" data-line-number="358" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">han_purple,"Han Purple",#5218fa,82,24,250</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R359" data-line-number="359" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">hansa_yellow,"Hansa Yellow",#e9d66b,233,214,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R360" data-line-number="360" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">harlequin,"Harlequin",#3fff00,63,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R361" data-line-number="361" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">harvard_crimson,"Harvard Crimson",#c90016,201,0,22</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R362" data-line-number="362" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">harvest_gold,"Harvest Gold",#da9100,218,145,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R363" data-line-number="363" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">heart_gold,"Heart Gold",#808000,128,128,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R364" data-line-number="364" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">heliotrope,"Heliotrope",#df73ff,223,115,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R365" data-line-number="365" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">hollywood_cerise,"Hollywood Cerise",#f400a1,244,0,161</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R366" data-line-number="366" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">honeydew,"Honeydew",#f0fff0,240,255,240</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R367" data-line-number="367" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">honolulu_blue,"Honolulu Blue",#007fbf,0,127,191</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R368" data-line-number="368" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">hooker_s_green,"Hooker'S Green",#49796b,73,121,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R369" data-line-number="369" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">hot_magenta,"Hot Magenta",#ff1dce,255,29,206</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R370" data-line-number="370" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">hot_pink,"Hot Pink",#ff69b4,255,105,180</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R371" data-line-number="371" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">hunter_green,"Hunter Green",#355e3b,53,94,59</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R372" data-line-number="372" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">iceberg,"Iceberg",#71a6d2,113,166,210</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R373" data-line-number="373" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">icterine,"Icterine",#fcf75e,252,247,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R374" data-line-number="374" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">imperial_blue,"Imperial Blue",#002395,0,35,149</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R375" data-line-number="375" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">inchworm,"Inchworm",#b2ec5d,178,236,93</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R376" data-line-number="376" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">india_green,"India Green",#138808,19,136,8</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R377" data-line-number="377" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">indian_red,"Indian Red",#cd5c5c,205,92,92</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R378" data-line-number="378" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">indian_yellow,"Indian Yellow",#e3a857,227,168,87</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R379" data-line-number="379" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">indigo,"Indigo",#6f00ff,111,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R380" data-line-number="380" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">indigo_dye,"Indigo (Dye)",#00416a,0,65,106</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R381" data-line-number="381" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">indigo_web,"Indigo (Web)",#4b0082,75,0,130</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R382" data-line-number="382" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">international_klein_blue,"International Klein Blue",#002fa7,0,47,167</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R383" data-line-number="383" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">international_orange_aerospace,"International Orange (Aerospace)",#ff4f00,255,79,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R384" data-line-number="384" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">international_orange_engineering,"International Orange (Engineering)",#ba160c,186,22,12</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R385" data-line-number="385" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">international_orange_golden_gate_bridge,"International Orange (Golden Gate Bridge)",#c0362c,192,54,44</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R386" data-line-number="386" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">iris,"Iris",#5a4fcf,90,79,207</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R387" data-line-number="387" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">isabelline,"Isabelline",#f4f0ec,244,240,236</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R388" data-line-number="388" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">islamic_green,"Islamic Green",#009000,0,144,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R389" data-line-number="389" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ivory,"Ivory",#fffff0,255,255,240</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R390" data-line-number="390" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">jade,"Jade",#00a86b,0,168,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R391" data-line-number="391" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">jasmine,"Jasmine",#f8de7e,248,222,126</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R392" data-line-number="392" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">jasper,"Jasper",#d73b3e,215,59,62</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R393" data-line-number="393" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">jazzberry_jam,"Jazzberry Jam",#a50b5e,165,11,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R394" data-line-number="394" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">jet,"Jet",#343434,52,52,52</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R395" data-line-number="395" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">jonquil,"Jonquil",#fada5e,250,218,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R396" data-line-number="396" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">june_bud,"June Bud",#bdda57,189,218,87</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R397" data-line-number="397" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">jungle_green,"Jungle Green",#29ab87,41,171,135</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R398" data-line-number="398" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">kelly_green,"Kelly Green",#4cbb17,76,187,23</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R399" data-line-number="399" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">kenyan_copper,"Kenyan Copper",#7c1c05,124,28,5</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R400" data-line-number="400" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">khaki_html_css_khaki,"Khaki (Html/Css) (Khaki)",#c3b091,195,176,145</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R401" data-line-number="401" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">khaki_x11_light_khaki,"Khaki (X11) (Light Khaki)",#f0e68c,240,230,140</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R402" data-line-number="402" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ku_crimson,"Ku Crimson",#e8000d,232,0,13</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R403" data-line-number="403" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">la_salle_green,"La Salle Green",#087830,8,120,48</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R404" data-line-number="404" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">languid_lavender,"Languid Lavender",#d6cadd,214,202,221</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R405" data-line-number="405" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lapis_lazuli,"Lapis Lazuli",#26619c,38,97,156</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R406" data-line-number="406" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">laser_lemon,"Laser Lemon",#fefe22,254,254,34</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R407" data-line-number="407" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">laurel_green,"Laurel Green",#a9ba9d,169,186,157</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R408" data-line-number="408" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lava,"Lava",#cf1020,207,16,32</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R409" data-line-number="409" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_blue,"Lavender Blue",#ccf,204,204,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R410" data-line-number="410" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_blush,"Lavender Blush",#fff0f5,255,240,245</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R411" data-line-number="411" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_floral,"Lavender (Floral)",#b57edc,181,126,220</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R412" data-line-number="412" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_gray,"Lavender Gray",#c4c3d0,196,195,208</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R413" data-line-number="413" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_indigo,"Lavender Indigo",#9457eb,148,87,235</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R414" data-line-number="414" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_magenta,"Lavender Magenta",#ee82ee,238,130,238</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R415" data-line-number="415" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_mist,"Lavender Mist",#e6e6fa,230,230,250</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R416" data-line-number="416" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_pink,"Lavender Pink",#fbaed2,251,174,210</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R417" data-line-number="417" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_purple,"Lavender Purple",#967bb6,150,123,182</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R418" data-line-number="418" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_rose,"Lavender Rose",#fba0e3,251,160,227</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R419" data-line-number="419" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lavender_web,"Lavender (Web)",#e6e6fa,230,230,250</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R420" data-line-number="420" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lawn_green,"Lawn Green",#7cfc00,124,252,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R421" data-line-number="421" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lemon,"Lemon",#fff700,255,247,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R422" data-line-number="422" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lemon_chiffon,"Lemon Chiffon",#fffacd,255,250,205</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R423" data-line-number="423" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lemon_lime,"Lemon Lime",#e3ff00,227,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R424" data-line-number="424" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">licorice,"Licorice",#1a1110,26,17,16</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R425" data-line-number="425" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_apricot,"Light Apricot",#fdd5b1,253,213,177</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R426" data-line-number="426" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_blue,"Light Blue",#add8e6,173,216,230</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R427" data-line-number="427" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_brown,"Light Brown",#b5651d,181,101,29</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R428" data-line-number="428" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_carmine_pink,"Light Carmine Pink",#e66771,230,103,113</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R429" data-line-number="429" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_coral,"Light Coral",#f08080,240,128,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R430" data-line-number="430" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_cornflower_blue,"Light Cornflower Blue",#93ccea,147,204,234</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R431" data-line-number="431" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_crimson,"Light Crimson",#f56991,245,105,145</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R432" data-line-number="432" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_cyan,"Light Cyan",#e0ffff,224,255,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R433" data-line-number="433" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_fuchsia_pink,"Light Fuchsia Pink",#f984ef,249,132,239</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R434" data-line-number="434" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_goldenrod_yellow,"Light Goldenrod Yellow",#fafad2,250,250,210</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R435" data-line-number="435" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_gray,"Light Gray",#d3d3d3,211,211,211</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R436" data-line-number="436" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_green,"Light Green",#90ee90,144,238,144</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R437" data-line-number="437" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_khaki,"Light Khaki",#f0e68c,240,230,140</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R438" data-line-number="438" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_pastel_purple,"Light Pastel Purple",#b19cd9,177,156,217</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R439" data-line-number="439" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_pink,"Light Pink",#ffb6c1,255,182,193</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R440" data-line-number="440" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_red_ochre,"Light Red Ochre",#e97451,233,116,81</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R441" data-line-number="441" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_salmon,"Light Salmon",#ffa07a,255,160,122</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R442" data-line-number="442" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_salmon_pink,"Light Salmon Pink",#f99,255,153,153</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R443" data-line-number="443" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_sea_green,"Light Sea Green",#20b2aa,32,178,170</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R444" data-line-number="444" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_sky_blue,"Light Sky Blue",#87cefa,135,206,250</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R445" data-line-number="445" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_slate_gray,"Light Slate Gray",#789,119,136,153</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R446" data-line-number="446" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_taupe,"Light Taupe",#b38b6d,179,139,109</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R447" data-line-number="447" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_thulian_pink,"Light Thulian Pink",#e68fac,230,143,172</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R448" data-line-number="448" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">light_yellow,"Light Yellow",#ffffe0,255,255,224</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R449" data-line-number="449" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lilac,"Lilac",#c8a2c8,200,162,200</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R450" data-line-number="450" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lime_color_wheel,"Lime (Color Wheel)",#bfff00,191,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R451" data-line-number="451" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lime_green,"Lime Green",#32cd32,50,205,50</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R452" data-line-number="452" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lime_web_x11_green,"Lime (Web) (X11 Green)",#0f0,0,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R453" data-line-number="453" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">limerick,"Limerick",#9dc209,157,194,9</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R454" data-line-number="454" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lincoln_green,"Lincoln Green",#195905,25,89,5</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R455" data-line-number="455" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">linen,"Linen",#faf0e6,250,240,230</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R456" data-line-number="456" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lion,"Lion",#c19a6b,193,154,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R457" data-line-number="457" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">little_boy_blue,"Little Boy Blue",#6ca0dc,108,160,220</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R458" data-line-number="458" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">liver,"Liver",#534b4f,83,75,79</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R459" data-line-number="459" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">lust,"Lust",#e62020,230,32,32</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R460" data-line-number="460" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">magenta,"Magenta",#f0f,255,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R461" data-line-number="461" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">magenta_dye,"Magenta (Dye)",#ca1f7b,202,31,123</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R462" data-line-number="462" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">magenta_process,"Magenta (Process)",#ff0090,255,0,144</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R463" data-line-number="463" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">magic_mint,"Magic Mint",#aaf0d1,170,240,209</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R464" data-line-number="464" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">magnolia,"Magnolia",#f8f4ff,248,244,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R465" data-line-number="465" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mahogany,"Mahogany",#c04000,192,64,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R466" data-line-number="466" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">maize,"Maize",#fbec5d,251,236,93</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R467" data-line-number="467" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">majorelle_blue,"Majorelle Blue",#6050dc,96,80,220</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R468" data-line-number="468" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">malachite,"Malachite",#0bda51,11,218,81</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R469" data-line-number="469" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">manatee,"Manatee",#979aaa,151,154,170</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R470" data-line-number="470" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mango_tango,"Mango Tango",#ff8243,255,130,67</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R471" data-line-number="471" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mantis,"Mantis",#74c365,116,195,101</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R472" data-line-number="472" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mardi_gras,"Mardi Gras",#880085,136,0,133</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R473" data-line-number="473" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">maroon_crayola,"Maroon (Crayola)",#c32148,195,33,72</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R474" data-line-number="474" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">maroon_html_css,"Maroon (Html/Css)",#800000,128,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R475" data-line-number="475" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">maroon_x11,"Maroon (X11)",#b03060,176,48,96</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R476" data-line-number="476" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mauve,"Mauve",#e0b0ff,224,176,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R477" data-line-number="477" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mauve_taupe,"Mauve Taupe",#915f6d,145,95,109</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R478" data-line-number="478" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mauvelous,"Mauvelous",#ef98aa,239,152,170</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R479" data-line-number="479" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">maya_blue,"Maya Blue",#73c2fb,115,194,251</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R480" data-line-number="480" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">meat_brown,"Meat Brown",#e5b73b,229,183,59</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R481" data-line-number="481" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_aquamarine,"Medium Aquamarine",#6da,102,221,170</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R482" data-line-number="482" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_blue,"Medium Blue",#0000cd,0,0,205</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R483" data-line-number="483" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_candy_apple_red,"Medium Candy Apple Red",#e2062c,226,6,44</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R484" data-line-number="484" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_carmine,"Medium Carmine",#af4035,175,64,53</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R485" data-line-number="485" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_champagne,"Medium Champagne",#f3e5ab,243,229,171</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R486" data-line-number="486" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_electric_blue,"Medium Electric Blue",#035096,3,80,150</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R487" data-line-number="487" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_jungle_green,"Medium Jungle Green",#1c352d,28,53,45</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R488" data-line-number="488" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_lavender_magenta,"Medium Lavender Magenta",#dda0dd,221,160,221</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R489" data-line-number="489" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_orchid,"Medium Orchid",#ba55d3,186,85,211</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R490" data-line-number="490" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_persian_blue,"Medium Persian Blue",#0067a5,0,103,165</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R491" data-line-number="491" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_purple,"Medium Purple",#9370db,147,112,219</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R492" data-line-number="492" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_red_violet,"Medium Red-Violet",#bb3385,187,51,133</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R493" data-line-number="493" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_ruby,"Medium Ruby",#aa4069,170,64,105</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R494" data-line-number="494" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_sea_green,"Medium Sea Green",#3cb371,60,179,113</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R495" data-line-number="495" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_slate_blue,"Medium Slate Blue",#7b68ee,123,104,238</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R496" data-line-number="496" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_spring_bud,"Medium Spring Bud",#c9dc87,201,220,135</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R497" data-line-number="497" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_spring_green,"Medium Spring Green",#00fa9a,0,250,154</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R498" data-line-number="498" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_taupe,"Medium Taupe",#674c47,103,76,71</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R499" data-line-number="499" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_turquoise,"Medium Turquoise",#48d1cc,72,209,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R500" data-line-number="500" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_tuscan_red,"Medium Tuscan Red",#79443b,121,68,59</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R501" data-line-number="501" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_vermilion,"Medium Vermilion",#d9603b,217,96,59</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R502" data-line-number="502" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">medium_violet_red,"Medium Violet-Red",#c71585,199,21,133</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R503" data-line-number="503" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mellow_apricot,"Mellow Apricot",#f8b878,248,184,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R504" data-line-number="504" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mellow_yellow,"Mellow Yellow",#f8de7e,248,222,126</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R505" data-line-number="505" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">melon,"Melon",#fdbcb4,253,188,180</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R506" data-line-number="506" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">midnight_blue,"Midnight Blue",#191970,25,25,112</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R507" data-line-number="507" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">midnight_green_eagle_green,"Midnight Green (Eagle Green)",#004953,0,73,83</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R508" data-line-number="508" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mikado_yellow,"Mikado Yellow",#ffc40c,255,196,12</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R509" data-line-number="509" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mint,"Mint",#3eb489,62,180,137</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R510" data-line-number="510" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mint_cream,"Mint Cream",#f5fffa,245,255,250</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R511" data-line-number="511" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mint_green,"Mint Green",#98ff98,152,255,152</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R512" data-line-number="512" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">misty_rose,"Misty Rose",#ffe4e1,255,228,225</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R513" data-line-number="513" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">moccasin,"Moccasin",#faebd7,250,235,215</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R514" data-line-number="514" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mode_beige,"Mode Beige",#967117,150,113,23</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R515" data-line-number="515" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">moonstone_blue,"Moonstone Blue",#73a9c2,115,169,194</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R516" data-line-number="516" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mordant_red_19,"Mordant Red 19",#ae0c00,174,12,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R517" data-line-number="517" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">moss_green,"Moss Green",#addfad,173,223,173</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R518" data-line-number="518" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mountain_meadow,"Mountain Meadow",#30ba8f,48,186,143</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R519" data-line-number="519" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mountbatten_pink,"Mountbatten Pink",#997a8d,153,122,141</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R520" data-line-number="520" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">msu_green,"Msu Green",#18453b,24,69,59</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R521" data-line-number="521" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mulberry,"Mulberry",#c54b8c,197,75,140</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R522" data-line-number="522" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">mustard,"Mustard",#ffdb58,255,219,88</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R523" data-line-number="523" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">myrtle,"Myrtle",#21421e,33,66,30</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R524" data-line-number="524" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">nadeshiko_pink,"Nadeshiko Pink",#f6adc6,246,173,198</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R525" data-line-number="525" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">napier_green,"Napier Green",#2a8000,42,128,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R526" data-line-number="526" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">naples_yellow,"Naples Yellow",#fada5e,250,218,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R527" data-line-number="527" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">navajo_white,"Navajo White",#ffdead,255,222,173</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R528" data-line-number="528" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">navy_blue,"Navy Blue",#000080,0,0,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R529" data-line-number="529" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">neon_carrot,"Neon Carrot",#ffa343,255,163,67</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R530" data-line-number="530" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">neon_fuchsia,"Neon Fuchsia",#fe4164,254,65,100</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R531" data-line-number="531" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">neon_green,"Neon Green",#39ff14,57,255,20</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R532" data-line-number="532" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">new_york_pink,"New York Pink",#d7837f,215,131,127</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R533" data-line-number="533" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">non_photo_blue,"Non-Photo Blue",#a4dded,164,221,237</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R534" data-line-number="534" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">north_texas_green,"North Texas Green",#059033,5,144,51</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R535" data-line-number="535" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ocean_boat_blue,"Ocean Boat Blue",#0077be,0,119,190</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R536" data-line-number="536" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ochre,"Ochre",#c72,204,119,34</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R537" data-line-number="537" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">office_green,"Office Green",#008000,0,128,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R538" data-line-number="538" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">old_gold,"Old Gold",#cfb53b,207,181,59</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R539" data-line-number="539" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">old_lace,"Old Lace",#fdf5e6,253,245,230</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R540" data-line-number="540" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">old_lavender,"Old Lavender",#796878,121,104,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R541" data-line-number="541" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">old_mauve,"Old Mauve",#673147,103,49,71</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R542" data-line-number="542" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">old_rose,"Old Rose",#c08081,192,128,129</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R543" data-line-number="543" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">olive,"Olive",#808000,128,128,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R544" data-line-number="544" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">olive_drab_7,"Olive Drab #7",#3c341f,60,52,31</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R545" data-line-number="545" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">olive_drab_web_olive_drab_3,"Olive Drab (Web) (Olive Drab #3)",#6b8e23,107,142,35</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R546" data-line-number="546" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">olivine,"Olivine",#9ab973,154,185,115</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R547" data-line-number="547" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">onyx,"Onyx",#353839,53,56,57</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R548" data-line-number="548" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">opera_mauve,"Opera Mauve",#b784a7,183,132,167</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R549" data-line-number="549" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">orange_color_wheel,"Orange (Color Wheel)",#ff7f00,255,127,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R550" data-line-number="550" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">orange_peel,"Orange Peel",#ff9f00,255,159,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R551" data-line-number="551" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">orange_red,"Orange-Red",#ff4500,255,69,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R552" data-line-number="552" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">orange_ryb,"Orange (Ryb)",#fb9902,251,153,2</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R553" data-line-number="553" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">orange_web_color,"Orange (Web Color)",#ffa500,255,165,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R554" data-line-number="554" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">orchid,"Orchid",#da70d6,218,112,214</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R555" data-line-number="555" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">otter_brown,"Otter Brown",#654321,101,67,33</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R556" data-line-number="556" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ou_crimson_red,"Ou Crimson Red",#900,153,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R557" data-line-number="557" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">outer_space,"Outer Space",#414a4c,65,74,76</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R558" data-line-number="558" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">outrageous_orange,"Outrageous Orange",#ff6e4a,255,110,74</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R559" data-line-number="559" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">oxford_blue,"Oxford Blue",#002147,0,33,71</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R560" data-line-number="560" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pakistan_green,"Pakistan Green",#060,0,102,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R561" data-line-number="561" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">palatinate_blue,"Palatinate Blue",#273be2,39,59,226</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R562" data-line-number="562" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">palatinate_purple,"Palatinate Purple",#682860,104,40,96</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R563" data-line-number="563" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_aqua,"Pale Aqua",#bcd4e6,188,212,230</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R564" data-line-number="564" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_blue,"Pale Blue",#afeeee,175,238,238</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R565" data-line-number="565" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_brown,"Pale Brown",#987654,152,118,84</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R566" data-line-number="566" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_carmine,"Pale Carmine",#af4035,175,64,53</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R567" data-line-number="567" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_cerulean,"Pale Cerulean",#9bc4e2,155,196,226</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R568" data-line-number="568" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_chestnut,"Pale Chestnut",#ddadaf,221,173,175</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R569" data-line-number="569" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_copper,"Pale Copper",#da8a67,218,138,103</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R570" data-line-number="570" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_cornflower_blue,"Pale Cornflower Blue",#abcdef,171,205,239</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R571" data-line-number="571" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_gold,"Pale Gold",#e6be8a,230,190,138</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R572" data-line-number="572" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_goldenrod,"Pale Goldenrod",#eee8aa,238,232,170</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R573" data-line-number="573" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_green,"Pale Green",#98fb98,152,251,152</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R574" data-line-number="574" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_lavender,"Pale Lavender",#dcd0ff,220,208,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R575" data-line-number="575" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_magenta,"Pale Magenta",#f984e5,249,132,229</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R576" data-line-number="576" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_pink,"Pale Pink",#fadadd,250,218,221</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R577" data-line-number="577" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_plum,"Pale Plum",#dda0dd,221,160,221</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R578" data-line-number="578" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_red_violet,"Pale Red-Violet",#db7093,219,112,147</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R579" data-line-number="579" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_robin_egg_blue,"Pale Robin Egg Blue",#96ded1,150,222,209</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R580" data-line-number="580" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_silver,"Pale Silver",#c9c0bb,201,192,187</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R581" data-line-number="581" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_spring_bud,"Pale Spring Bud",#ecebbd,236,235,189</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R582" data-line-number="582" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_taupe,"Pale Taupe",#bc987e,188,152,126</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R583" data-line-number="583" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pale_violet_red,"Pale Violet-Red",#db7093,219,112,147</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R584" data-line-number="584" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pansy_purple,"Pansy Purple",#78184a,120,24,74</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R585" data-line-number="585" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">papaya_whip,"Papaya Whip",#ffefd5,255,239,213</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R586" data-line-number="586" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">paris_green,"Paris Green",#50c878,80,200,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R587" data-line-number="587" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_blue,"Pastel Blue",#aec6cf,174,198,207</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R588" data-line-number="588" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_brown,"Pastel Brown",#836953,131,105,83</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R589" data-line-number="589" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_gray,"Pastel Gray",#cfcfc4,207,207,196</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R590" data-line-number="590" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_green,"Pastel Green",#7d7,119,221,119</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R591" data-line-number="591" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_magenta,"Pastel Magenta",#f49ac2,244,154,194</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R592" data-line-number="592" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_orange,"Pastel Orange",#ffb347,255,179,71</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R593" data-line-number="593" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_pink,"Pastel Pink",#dea5a4,222,165,164</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R594" data-line-number="594" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_purple,"Pastel Purple",#b39eb5,179,158,181</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R595" data-line-number="595" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_red,"Pastel Red",#ff6961,255,105,97</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R596" data-line-number="596" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_violet,"Pastel Violet",#cb99c9,203,153,201</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R597" data-line-number="597" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pastel_yellow,"Pastel Yellow",#fdfd96,253,253,150</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R598" data-line-number="598" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">patriarch,"Patriarch",#800080,128,0,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R599" data-line-number="599" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">payne_s_grey,"Payne'S Grey",#536878,83,104,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R600" data-line-number="600" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">peach,"Peach",#ffe5b4,255,229,180</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R601" data-line-number="601" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">peach_crayola,"Peach (Crayola)",#ffcba4,255,203,164</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R602" data-line-number="602" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">peach_orange,"Peach-Orange",#fc9,255,204,153</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R603" data-line-number="603" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">peach_puff,"Peach Puff",#ffdab9,255,218,185</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R604" data-line-number="604" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">peach_yellow,"Peach-Yellow",#fadfad,250,223,173</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R605" data-line-number="605" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pear,"Pear",#d1e231,209,226,49</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R606" data-line-number="606" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pearl,"Pearl",#eae0c8,234,224,200</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R607" data-line-number="607" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pearl_aqua,"Pearl Aqua",#88d8c0,136,216,192</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R608" data-line-number="608" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pearly_purple,"Pearly Purple",#b768a2,183,104,162</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R609" data-line-number="609" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">peridot,"Peridot",#e6e200,230,226,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R610" data-line-number="610" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">periwinkle,"Periwinkle",#ccf,204,204,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R611" data-line-number="611" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persian_blue,"Persian Blue",#1c39bb,28,57,187</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R612" data-line-number="612" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persian_green,"Persian Green",#00a693,0,166,147</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R613" data-line-number="613" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persian_indigo,"Persian Indigo",#32127a,50,18,122</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R614" data-line-number="614" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persian_orange,"Persian Orange",#d99058,217,144,88</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R615" data-line-number="615" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persian_pink,"Persian Pink",#f77fbe,247,127,190</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R616" data-line-number="616" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persian_plum,"Persian Plum",#701c1c,112,28,28</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R617" data-line-number="617" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persian_red,"Persian Red",#c33,204,51,51</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R618" data-line-number="618" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persian_rose,"Persian Rose",#fe28a2,254,40,162</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R619" data-line-number="619" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">persimmon,"Persimmon",#ec5800,236,88,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R620" data-line-number="620" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">peru,"Peru",#cd853f,205,133,63</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R621" data-line-number="621" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">phlox,"Phlox",#df00ff,223,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R622" data-line-number="622" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">phthalo_blue,"Phthalo Blue",#000f89,0,15,137</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R623" data-line-number="623" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">phthalo_green,"Phthalo Green",#123524,18,53,36</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R624" data-line-number="624" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">piggy_pink,"Piggy Pink",#fddde6,253,221,230</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R625" data-line-number="625" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pine_green,"Pine Green",#01796f,1,121,111</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R626" data-line-number="626" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pink,"Pink",#ffc0cb,255,192,203</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R627" data-line-number="627" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pink_lace,"Pink Lace",#ffddf4,255,221,244</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R628" data-line-number="628" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pink_orange,"Pink-Orange",#f96,255,153,102</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R629" data-line-number="629" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pink_pearl,"Pink Pearl",#e7accf,231,172,207</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R630" data-line-number="630" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pink_sherbet,"Pink Sherbet",#f78fa7,247,143,167</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R631" data-line-number="631" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pistachio,"Pistachio",#93c572,147,197,114</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R632" data-line-number="632" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">platinum,"Platinum",#e5e4e2,229,228,226</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R633" data-line-number="633" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">plum_traditional,"Plum (Traditional)",#8e4585,142,69,133</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R634" data-line-number="634" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">plum_web,"Plum (Web)",#dda0dd,221,160,221</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R635" data-line-number="635" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">portland_orange,"Portland Orange",#ff5a36,255,90,54</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R636" data-line-number="636" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">powder_blue_web,"Powder Blue (Web)",#b0e0e6,176,224,230</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R637" data-line-number="637" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">princeton_orange,"Princeton Orange",#ff8f00,255,143,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R638" data-line-number="638" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">prune,"Prune",#701c1c,112,28,28</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R639" data-line-number="639" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">prussian_blue,"Prussian Blue",#003153,0,49,83</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R640" data-line-number="640" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">psychedelic_purple,"Psychedelic Purple",#df00ff,223,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R641" data-line-number="641" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">puce,"Puce",#c89,204,136,153</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R642" data-line-number="642" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">pumpkin,"Pumpkin",#ff7518,255,117,24</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R643" data-line-number="643" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">purple_heart,"Purple Heart",#69359c,105,53,156</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R644" data-line-number="644" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">purple_html_css,"Purple (Html/Css)",#800080,128,0,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R645" data-line-number="645" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">purple_mountain_majesty,"Purple Mountain Majesty",#9678b6,150,120,182</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R646" data-line-number="646" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">purple_munsell,"Purple (Munsell)",#9f00c5,159,0,197</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R647" data-line-number="647" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">purple_pizzazz,"Purple Pizzazz",#fe4eda,254,78,218</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R648" data-line-number="648" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">purple_taupe,"Purple Taupe",#50404d,80,64,77</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R649" data-line-number="649" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">purple_x11,"Purple (X11)",#a020f0,160,32,240</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R650" data-line-number="650" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">quartz,"Quartz",#51484f,81,72,79</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R651" data-line-number="651" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rackley,"Rackley",#5d8aa8,93,138,168</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R652" data-line-number="652" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">radical_red,"Radical Red",#ff355e,255,53,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R653" data-line-number="653" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rajah,"Rajah",#fbab60,251,171,96</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R654" data-line-number="654" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">raspberry,"Raspberry",#e30b5d,227,11,93</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R655" data-line-number="655" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">raspberry_glace,"Raspberry Glace",#915f6d,145,95,109</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R656" data-line-number="656" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">raspberry_pink,"Raspberry Pink",#e25098,226,80,152</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R657" data-line-number="657" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">raspberry_rose,"Raspberry Rose",#b3446c,179,68,108</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R658" data-line-number="658" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">raw_umber,"Raw Umber",#826644,130,102,68</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R659" data-line-number="659" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">razzle_dazzle_rose,"Razzle Dazzle Rose",#f3c,255,51,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R660" data-line-number="660" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">razzmatazz,"Razzmatazz",#e3256b,227,37,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R661" data-line-number="661" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red,"Red",#f00,255,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R662" data-line-number="662" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red_brown,"Red-Brown",#a52a2a,165,42,42</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R663" data-line-number="663" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red_devil,"Red Devil",#860111,134,1,17</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R664" data-line-number="664" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red_munsell,"Red (Munsell)",#f2003c,242,0,60</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R665" data-line-number="665" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red_ncs,"Red (Ncs)",#c40233,196,2,51</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R666" data-line-number="666" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red_orange,"Red-Orange",#ff5349,255,83,73</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R667" data-line-number="667" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red_pigment,"Red (Pigment)",#ed1c24,237,28,36</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R668" data-line-number="668" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red_ryb,"Red (Ryb)",#fe2712,254,39,18</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R669" data-line-number="669" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">red_violet,"Red-Violet",#c71585,199,21,133</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R670" data-line-number="670" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">redwood,"Redwood",#ab4e52,171,78,82</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R671" data-line-number="671" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">regalia,"Regalia",#522d80,82,45,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R672" data-line-number="672" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">resolution_blue,"Resolution Blue",#002387,0,35,135</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R673" data-line-number="673" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rich_black,"Rich Black",#004040,0,64,64</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R674" data-line-number="674" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rich_brilliant_lavender,"Rich Brilliant Lavender",#f1a7fe,241,167,254</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R675" data-line-number="675" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rich_carmine,"Rich Carmine",#d70040,215,0,64</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R676" data-line-number="676" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rich_electric_blue,"Rich Electric Blue",#0892d0,8,146,208</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R677" data-line-number="677" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rich_lavender,"Rich Lavender",#a76bcf,167,107,207</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R678" data-line-number="678" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rich_lilac,"Rich Lilac",#b666d2,182,102,210</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R679" data-line-number="679" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rich_maroon,"Rich Maroon",#b03060,176,48,96</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R680" data-line-number="680" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rifle_green,"Rifle Green",#414833,65,72,51</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R681" data-line-number="681" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">robin_egg_blue,"Robin Egg Blue",#0cc,0,204,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R682" data-line-number="682" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose,"Rose",#ff007f,255,0,127</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R683" data-line-number="683" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose_bonbon,"Rose Bonbon",#f9429e,249,66,158</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R684" data-line-number="684" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose_ebony,"Rose Ebony",#674846,103,72,70</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R685" data-line-number="685" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose_gold,"Rose Gold",#b76e79,183,110,121</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R686" data-line-number="686" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose_madder,"Rose Madder",#e32636,227,38,54</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R687" data-line-number="687" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose_pink,"Rose Pink",#f6c,255,102,204</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R688" data-line-number="688" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose_quartz,"Rose Quartz",#aa98a9,170,152,169</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R689" data-line-number="689" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose_taupe,"Rose Taupe",#905d5d,144,93,93</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R690" data-line-number="690" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rose_vale,"Rose Vale",#ab4e52,171,78,82</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R691" data-line-number="691" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rosewood,"Rosewood",#65000b,101,0,11</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R692" data-line-number="692" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rosso_corsa,"Rosso Corsa",#d40000,212,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R693" data-line-number="693" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rosy_brown,"Rosy Brown",#bc8f8f,188,143,143</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R694" data-line-number="694" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">royal_azure,"Royal Azure",#0038a8,0,56,168</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R695" data-line-number="695" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">royal_blue_traditional,"Royal Blue (Traditional)",#002366,0,35,102</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R696" data-line-number="696" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">royal_blue_web,"Royal Blue (Web)",#4169e1,65,105,225</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R697" data-line-number="697" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">royal_fuchsia,"Royal Fuchsia",#ca2c92,202,44,146</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R698" data-line-number="698" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">royal_purple,"Royal Purple",#7851a9,120,81,169</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R699" data-line-number="699" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">royal_yellow,"Royal Yellow",#fada5e,250,218,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R700" data-line-number="700" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rubine_red,"Rubine Red",#d10056,209,0,86</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R701" data-line-number="701" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ruby,"Ruby",#e0115f,224,17,95</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R702" data-line-number="702" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ruby_red,"Ruby Red",#9b111e,155,17,30</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R703" data-line-number="703" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ruddy,"Ruddy",#ff0028,255,0,40</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R704" data-line-number="704" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ruddy_brown,"Ruddy Brown",#bb6528,187,101,40</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R705" data-line-number="705" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ruddy_pink,"Ruddy Pink",#e18e96,225,142,150</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R706" data-line-number="706" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rufous,"Rufous",#a81c07,168,28,7</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R707" data-line-number="707" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">russet,"Russet",#80461b,128,70,27</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R708" data-line-number="708" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rust,"Rust",#b7410e,183,65,14</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R709" data-line-number="709" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">rusty_red,"Rusty Red",#da2c43,218,44,67</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R710" data-line-number="710" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sacramento_state_green,"Sacramento State Green",#00563f,0,86,63</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R711" data-line-number="711" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">saddle_brown,"Saddle Brown",#8b4513,139,69,19</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R712" data-line-number="712" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">safety_orange_blaze_orange,"Safety Orange (Blaze Orange)",#ff6700,255,103,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R713" data-line-number="713" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">saffron,"Saffron",#f4c430,244,196,48</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R714" data-line-number="714" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">salmon,"Salmon",#ff8c69,255,140,105</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R715" data-line-number="715" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">salmon_pink,"Salmon Pink",#ff91a4,255,145,164</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R716" data-line-number="716" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sand,"Sand",#c2b280,194,178,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R717" data-line-number="717" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sand_dune,"Sand Dune",#967117,150,113,23</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R718" data-line-number="718" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sandstorm,"Sandstorm",#ecd540,236,213,64</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R719" data-line-number="719" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sandy_brown,"Sandy Brown",#f4a460,244,164,96</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R720" data-line-number="720" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sandy_taupe,"Sandy Taupe",#967117,150,113,23</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R721" data-line-number="721" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sangria,"Sangria",#92000a,146,0,10</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R722" data-line-number="722" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sap_green,"Sap Green",#507d2a,80,125,42</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R723" data-line-number="723" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sapphire,"Sapphire",#0f52ba,15,82,186</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R724" data-line-number="724" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sapphire_blue,"Sapphire Blue",#0067a5,0,103,165</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R725" data-line-number="725" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">satin_sheen_gold,"Satin Sheen Gold",#cba135,203,161,53</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R726" data-line-number="726" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">scarlet,"Scarlet",#ff2400,255,36,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R727" data-line-number="727" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">scarlet_crayola,"Scarlet (Crayola)",#fd0e35,253,14,53</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R728" data-line-number="728" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">school_bus_yellow,"School Bus Yellow",#ffd800,255,216,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R729" data-line-number="729" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">screamin_green,"Screamin' Green",#76ff7a,118,255,122</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R730" data-line-number="730" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sea_blue,"Sea Blue",#006994,0,105,148</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R731" data-line-number="731" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sea_green,"Sea Green",#2e8b57,46,139,87</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R732" data-line-number="732" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">seal_brown,"Seal Brown",#321414,50,20,20</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R733" data-line-number="733" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">seashell,"Seashell",#fff5ee,255,245,238</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R734" data-line-number="734" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">selective_yellow,"Selective Yellow",#ffba00,255,186,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R735" data-line-number="735" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sepia,"Sepia",#704214,112,66,20</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R736" data-line-number="736" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">shadow,"Shadow",#8a795d,138,121,93</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R737" data-line-number="737" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">shamrock_green,"Shamrock Green",#009e60,0,158,96</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R738" data-line-number="738" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">shocking_pink,"Shocking Pink",#fc0fc0,252,15,192</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R739" data-line-number="739" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">shocking_pink_crayola,"Shocking Pink (Crayola)",#ff6fff,255,111,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R740" data-line-number="740" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sienna,"Sienna",#882d17,136,45,23</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R741" data-line-number="741" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">silver,"Silver",#c0c0c0,192,192,192</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R742" data-line-number="742" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sinopia,"Sinopia",#cb410b,203,65,11</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R743" data-line-number="743" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">skobeloff,"Skobeloff",#007474,0,116,116</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R744" data-line-number="744" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sky_blue,"Sky Blue",#87ceeb,135,206,235</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R745" data-line-number="745" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sky_magenta,"Sky Magenta",#cf71af,207,113,175</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R746" data-line-number="746" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">slate_blue,"Slate Blue",#6a5acd,106,90,205</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R747" data-line-number="747" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">slate_gray,"Slate Gray",#708090,112,128,144</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R748" data-line-number="748" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">smalt_dark_powder_blue,"Smalt (Dark Powder Blue)",#039,0,51,153</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R749" data-line-number="749" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">smokey_topaz,"Smokey Topaz",#933d41,147,61,65</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R750" data-line-number="750" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">smoky_black,"Smoky Black",#100c08,16,12,8</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R751" data-line-number="751" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">snow,"Snow",#fffafa,255,250,250</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R752" data-line-number="752" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">spiro_disco_ball,"Spiro Disco Ball",#0fc0fc,15,192,252</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R753" data-line-number="753" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">spring_bud,"Spring Bud",#a7fc00,167,252,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R754" data-line-number="754" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">spring_green,"Spring Green",#00ff7f,0,255,127</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R755" data-line-number="755" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">st_patrick_s_blue,"St. Patrick'S Blue",#23297a,35,41,122</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R756" data-line-number="756" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">steel_blue,"Steel Blue",#4682b4,70,130,180</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R757" data-line-number="757" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">stil_de_grain_yellow,"Stil De Grain Yellow",#fada5e,250,218,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R758" data-line-number="758" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">stizza,"Stizza",#900,153,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R759" data-line-number="759" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">stormcloud,"Stormcloud",#4f666a,79,102,106</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R760" data-line-number="760" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">straw,"Straw",#e4d96f,228,217,111</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R761" data-line-number="761" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sunglow,"Sunglow",#fc3,255,204,51</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R762" data-line-number="762" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">sunset,"Sunset",#fad6a5,250,214,165</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R763" data-line-number="763" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tan,"Tan",#d2b48c,210,180,140</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R764" data-line-number="764" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tangelo,"Tangelo",#f94d00,249,77,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R765" data-line-number="765" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tangerine,"Tangerine",#f28500,242,133,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R766" data-line-number="766" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tangerine_yellow,"Tangerine Yellow",#fc0,255,204,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R767" data-line-number="767" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tango_pink,"Tango Pink",#e4717a,228,113,122</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R768" data-line-number="768" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">taupe,"Taupe",#483c32,72,60,50</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R769" data-line-number="769" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">taupe_gray,"Taupe Gray",#8b8589,139,133,137</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R770" data-line-number="770" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tea_green,"Tea Green",#d0f0c0,208,240,192</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R771" data-line-number="771" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tea_rose_orange,"Tea Rose (Orange)",#f88379,248,131,121</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R772" data-line-number="772" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tea_rose_rose,"Tea Rose (Rose)",#f4c2c2,244,194,194</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R773" data-line-number="773" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">teal,"Teal",#008080,0,128,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R774" data-line-number="774" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">teal_blue,"Teal Blue",#367588,54,117,136</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R775" data-line-number="775" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">teal_green,"Teal Green",#00827f,0,130,127</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R776" data-line-number="776" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">telemagenta,"Telemagenta",#cf3476,207,52,118</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R777" data-line-number="777" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tenn_tawny,"Tenné (Tawny)",#cd5700,205,87,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R778" data-line-number="778" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">terra_cotta,"Terra Cotta",#e2725b,226,114,91</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R779" data-line-number="779" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">thistle,"Thistle",#d8bfd8,216,191,216</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R780" data-line-number="780" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">thulian_pink,"Thulian Pink",#de6fa1,222,111,161</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R781" data-line-number="781" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tickle_me_pink,"Tickle Me Pink",#fc89ac,252,137,172</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R782" data-line-number="782" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tiffany_blue,"Tiffany Blue",#0abab5,10,186,181</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R783" data-line-number="783" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tiger_s_eye,"Tiger'S Eye",#e08d3c,224,141,60</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R784" data-line-number="784" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">timberwolf,"Timberwolf",#dbd7d2,219,215,210</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R785" data-line-number="785" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">titanium_yellow,"Titanium Yellow",#eee600,238,230,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R786" data-line-number="786" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tomato,"Tomato",#ff6347,255,99,71</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R787" data-line-number="787" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">toolbox,"Toolbox",#746cc0,116,108,192</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R788" data-line-number="788" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">topaz,"Topaz",#ffc87c,255,200,124</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R789" data-line-number="789" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tractor_red,"Tractor Red",#fd0e35,253,14,53</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R790" data-line-number="790" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">trolley_grey,"Trolley Grey",#808080,128,128,128</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R791" data-line-number="791" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tropical_rain_forest,"Tropical Rain Forest",#00755e,0,117,94</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R792" data-line-number="792" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">true_blue,"True Blue",#0073cf,0,115,207</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R793" data-line-number="793" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tufts_blue,"Tufts Blue",#417dc1,65,125,193</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R794" data-line-number="794" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tumbleweed,"Tumbleweed",#deaa88,222,170,136</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R795" data-line-number="795" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">turkish_rose,"Turkish Rose",#b57281,181,114,129</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R796" data-line-number="796" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">turquoise,"Turquoise",#30d5c8,48,213,200</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R797" data-line-number="797" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">turquoise_blue,"Turquoise Blue",#00ffef,0,255,239</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R798" data-line-number="798" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">turquoise_green,"Turquoise Green",#a0d6b4,160,214,180</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R799" data-line-number="799" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tuscan_red,"Tuscan Red",#7c4848,124,72,72</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R800" data-line-number="800" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">twilight_lavender,"Twilight Lavender",#8a496b,138,73,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R801" data-line-number="801" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">tyrian_purple,"Tyrian Purple",#66023c,102,2,60</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R802" data-line-number="802" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ua_blue,"Ua Blue",#03a,0,51,170</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R803" data-line-number="803" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ua_red,"Ua Red",#d9004c,217,0,76</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R804" data-line-number="804" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ube,"Ube",#8878c3,136,120,195</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R805" data-line-number="805" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ucla_blue,"Ucla Blue",#536895,83,104,149</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R806" data-line-number="806" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ucla_gold,"Ucla Gold",#ffb300,255,179,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R807" data-line-number="807" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ufo_green,"Ufo Green",#3cd070,60,208,112</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R808" data-line-number="808" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ultra_pink,"Ultra Pink",#ff6fff,255,111,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R809" data-line-number="809" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ultramarine,"Ultramarine",#120a8f,18,10,143</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R810" data-line-number="810" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">ultramarine_blue,"Ultramarine Blue",#4166f5,65,102,245</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R811" data-line-number="811" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">umber,"Umber",#635147,99,81,71</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R812" data-line-number="812" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">unbleached_silk,"Unbleached Silk",#ffddca,255,221,202</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R813" data-line-number="813" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">united_nations_blue,"United Nations Blue",#5b92e5,91,146,229</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R814" data-line-number="814" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">university_of_california_gold,"University Of California Gold",#b78727,183,135,39</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R815" data-line-number="815" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">unmellow_yellow,"Unmellow Yellow",#ff6,255,255,102</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R816" data-line-number="816" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">up_forest_green,"Up Forest Green",#014421,1,68,33</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R817" data-line-number="817" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">up_maroon,"Up Maroon",#7b1113,123,17,19</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R818" data-line-number="818" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">upsdell_red,"Upsdell Red",#ae2029,174,32,41</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R819" data-line-number="819" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">urobilin,"Urobilin",#e1ad21,225,173,33</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R820" data-line-number="820" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">usafa_blue,"Usafa Blue",#004f98,0,79,152</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R821" data-line-number="821" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">usc_cardinal,"Usc Cardinal",#900,153,0,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R822" data-line-number="822" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">usc_gold,"Usc Gold",#fc0,255,204,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R823" data-line-number="823" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">utah_crimson,"Utah Crimson",#d3003f,211,0,63</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R824" data-line-number="824" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vanilla,"Vanilla",#f3e5ab,243,229,171</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R825" data-line-number="825" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vegas_gold,"Vegas Gold",#c5b358,197,179,88</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R826" data-line-number="826" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">venetian_red,"Venetian Red",#c80815,200,8,21</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R827" data-line-number="827" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">verdigris,"Verdigris",#43b3ae,67,179,174</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R828" data-line-number="828" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vermilion_cinnabar,"Vermilion (Cinnabar)",#e34234,227,66,52</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R829" data-line-number="829" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vermilion_plochere,"Vermilion (Plochere)",#d9603b,217,96,59</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R830" data-line-number="830" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">veronica,"Veronica",#a020f0,160,32,240</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R831" data-line-number="831" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">violet,"Violet",#8f00ff,143,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R832" data-line-number="832" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">violet_blue,"Violet-Blue",#324ab2,50,74,178</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R833" data-line-number="833" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">violet_color_wheel,"Violet (Color Wheel)",#7f00ff,127,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R834" data-line-number="834" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">violet_ryb,"Violet (Ryb)",#8601af,134,1,175</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R835" data-line-number="835" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">violet_web,"Violet (Web)",#ee82ee,238,130,238</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R836" data-line-number="836" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">viridian,"Viridian",#40826d,64,130,109</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R837" data-line-number="837" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vivid_auburn,"Vivid Auburn",#922724,146,39,36</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R838" data-line-number="838" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vivid_burgundy,"Vivid Burgundy",#9f1d35,159,29,53</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R839" data-line-number="839" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vivid_cerise,"Vivid Cerise",#da1d81,218,29,129</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R840" data-line-number="840" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vivid_tangerine,"Vivid Tangerine",#ffa089,255,160,137</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R841" data-line-number="841" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">vivid_violet,"Vivid Violet",#9f00ff,159,0,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R842" data-line-number="842" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">warm_black,"Warm Black",#004242,0,66,66</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R843" data-line-number="843" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">waterspout,"Waterspout",#a4f4f9,164,244,249</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R844" data-line-number="844" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wenge,"Wenge",#645452,100,84,82</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R845" data-line-number="845" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wheat,"Wheat",#f5deb3,245,222,179</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R846" data-line-number="846" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">white,"White",#fff,255,255,255</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R847" data-line-number="847" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">white_smoke,"White Smoke",#f5f5f5,245,245,245</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R848" data-line-number="848" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wild_blue_yonder,"Wild Blue Yonder",#a2add0,162,173,208</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R849" data-line-number="849" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wild_strawberry,"Wild Strawberry",#ff43a4,255,67,164</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R850" data-line-number="850" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wild_watermelon,"Wild Watermelon",#fc6c85,252,108,133</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R851" data-line-number="851" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wine,"Wine",#722f37,114,47,55</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R852" data-line-number="852" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wine_dregs,"Wine Dregs",#673147,103,49,71</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R853" data-line-number="853" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wisteria,"Wisteria",#c9a0dc,201,160,220</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R854" data-line-number="854" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">wood_brown,"Wood Brown",#c19a6b,193,154,107</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R855" data-line-number="855" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">xanadu,"Xanadu",#738678,115,134,120</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R856" data-line-number="856" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">yale_blue,"Yale Blue",#0f4d92,15,77,146</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R857" data-line-number="857" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">yellow,"Yellow",#ff0,255,255,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R858" data-line-number="858" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">yellow_green,"Yellow-Green",#9acd32,154,205,50</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R859" data-line-number="859" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">yellow_munsell,"Yellow (Munsell)",#efcc00,239,204,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R860" data-line-number="860" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">yellow_ncs,"Yellow (Ncs)",#ffd300,255,211,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R861" data-line-number="861" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">yellow_orange,"Yellow Orange",#ffae42,255,174,66</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R862" data-line-number="862" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">yellow_process,"Yellow (Process)",#ffef00,255,239,0</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R863" data-line-number="863" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">yellow_ryb,"Yellow (Ryb)",#fefe33,254,254,51</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R864" data-line-number="864" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">zaffre,"Zaffre",#0014a8,0,20,168</span></td>
</tr>




    <tr data-hunk="34e23e093298f2a9d17fc08a018ae851c99a45daad9cb4da15d827993c1f9796" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-d3dd53c133f1e18000a968a4b934a098670e73f2c9d6f068853c95874e8fc604R865" data-line-number="865" class="blob-num blob-num-addition js-linkable-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
    <span class="blob-code-inner blob-code-marker " data-code-marker="+">zinnwaldite_brown,"Zinnwaldite Brown",#2c1608,44,22,8</span></td>
</tr>






                </tbody>
              </table>

          </div>

</div>


    </div>
  </div>
</copilot-diff-entry>

  <copilot-diff-entry data-file-path="pic1.jpg" data-disabled="">
  <div id="diff-447ae593a2fad01339a71185cf2d139a5e3aaa2007f000cca356eff4c928b09d" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
               display-rich-diff
              
              
              " data-file-type=".jpg" data-file-deleted="false" data-tagsearch-path="pic1.jpg" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch" data-path="pic1.jpg" data-short-path="447ae59" data-anchor="diff-447ae593a2fad01339a71185cf2d139a5e3aaa2007f000cca356eff4c928b09d" data-file-type=".jpg" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">Binary file added</span>
          <span class="diffstat" aria-hidden="true">
            BIN
              <span class="color-fg-success">
                +1.9 MB

              </span>
          </span>

        
<span class="Truncate">
  <a title="pic1.jpg" class="Link--primary Truncate-text" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-447ae593a2fad01339a71185cf2d139a5e3aaa2007f000cca356eff4c928b09d">pic1.jpg</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="pic1.jpg" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">








            <span class="BtnGroup min-width-0">
                <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-prose-diff-toggle-form" data-turbo="false" action="https://github.com/Bansodeprasad/Color-Detection-/diffs/3?commit=d2de12dff17aff39101e04671cb502efb8330376&amp;name=main&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;source=true&amp;w=false" accept-charset="UTF-8" method="get">                  <button class="btn btn-sm BtnGroup-item tooltipped tooltipped-s source js-source" aria-label="Display the source diff" type="submit" data-disable-with="">
                          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
                  </button>
</form>                  <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-prose-diff-toggle-form" data-turbo="false" action="https://github.com/Bansodeprasad/Color-Detection-/diffs/3?commit=d2de12dff17aff39101e04671cb502efb8330376&amp;name=main&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;short_path=447ae59&amp;w=false" accept-charset="UTF-8" method="get">                    <button class="btn btn-sm BtnGroup-item tooltipped tooltipped-s rendered js-rendered selected" aria-current="true" aria-label="Display the rich diff" type="submit" data-disable-with="">
                            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file">
    <path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
                    </button>
</form>            </span>



          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:max-content; min-width:185px; z-index:99; right: -4px;" role="menu">
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/Bansodeprasad/Color-Detection-/blob/d2de12dff17aff39101e04671cb502efb8330376/pic1.jpg" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            </details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:null,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/diffs?bytes=2054&amp;commit=d2de12dff17aff39101e04671cb502efb8330376&amp;lines=70&amp;responsive=true&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;start_entry=2&amp;sticky=false&amp;w=false&quot;,&quot;user_id&quot;:null}}" data-hydro-view-hmac="da27f168452f5401cc39365cfa7bab7808b0055f832c759ca5c44e87de6005c1">
            <div class="render-wrapper ">
    <div class="render-container js-render-target is-render-automatic is-render-requested is-render-ready" data-identity="5eb07428-3d77-4e48-b62f-28749822398d" data-host="https://viewscreen.githubusercontent.com" data-type="img" style="height: 959.909px;">
      <span data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="64" height="64" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="octospinner mx-auto anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
      <div class="render-viewer-error">Sorry, something went wrong. <a class="Link--inTextBlock" href="https://github.com/Bansodeprasad/Color-Detection-/diffs?bytes=2054&amp;commit=d2de12dff17aff39101e04671cb502efb8330376&amp;lines=70&amp;responsive=true&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;start_entry=2&amp;sticky=false&amp;w=false">Reload?</a></div>
      <div class="render-viewer-fatal">Sorry, we cannot display this file.</div>
      <div class="render-viewer-invalid">Sorry, this file is invalid so it cannot be displayed.</div>
      <iframe class="render-viewer " src="./color_detection_files/img(1).html" sandbox="allow-scripts allow-same-origin allow-top-navigation" title="File display" name="5eb07428-3d77-4e48-b62f-28749822398d">
          Viewer requires iframe.
      </iframe>
    </div>
  </div>
 

    </div>
  </div>
</copilot-diff-entry>

  <copilot-diff-entry data-file-path="pic2.jpg" data-disabled="">
  <div id="diff-9c58f54e3b2ddd94f1d884d6564dbacf41f1a3e77d88ca110edc361f186657ef" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
               display-rich-diff
              
              
              " data-file-type=".jpg" data-file-deleted="false" data-tagsearch-path="pic2.jpg" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch" data-path="pic2.jpg" data-short-path="9c58f54" data-anchor="diff-9c58f54e3b2ddd94f1d884d6564dbacf41f1a3e77d88ca110edc361f186657ef" data-file-type=".jpg" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">Binary file added</span>
          <span class="diffstat" aria-hidden="true">
            BIN
              <span class="color-fg-success">
                +1.22 MB

              </span>
          </span>

        
<span class="Truncate">
  <a title="pic2.jpg" class="Link--primary Truncate-text" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-9c58f54e3b2ddd94f1d884d6564dbacf41f1a3e77d88ca110edc361f186657ef">pic2.jpg</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="pic2.jpg" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">








            <span class="BtnGroup min-width-0">
                <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-prose-diff-toggle-form" data-turbo="false" action="https://github.com/Bansodeprasad/Color-Detection-/diffs/4?commit=d2de12dff17aff39101e04671cb502efb8330376&amp;name=main&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;source=true&amp;w=false" accept-charset="UTF-8" method="get">                  <button class="btn btn-sm BtnGroup-item tooltipped tooltipped-s source js-source" aria-label="Display the source diff" type="submit" data-disable-with="">
                          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
                  </button>
</form>                  <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-prose-diff-toggle-form" data-turbo="false" action="https://github.com/Bansodeprasad/Color-Detection-/diffs/4?commit=d2de12dff17aff39101e04671cb502efb8330376&amp;name=main&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;short_path=9c58f54&amp;w=false" accept-charset="UTF-8" method="get">                    <button class="btn btn-sm BtnGroup-item tooltipped tooltipped-s rendered js-rendered selected" aria-current="true" aria-label="Display the rich diff" type="submit" data-disable-with="">
                            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file">
    <path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
                    </button>
</form>            </span>



          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:max-content; min-width:185px; z-index:99; right: -4px;" role="menu">
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/Bansodeprasad/Color-Detection-/blob/d2de12dff17aff39101e04671cb502efb8330376/pic2.jpg" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            </details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:null,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/diffs?bytes=2054&amp;commit=d2de12dff17aff39101e04671cb502efb8330376&amp;lines=70&amp;responsive=true&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;start_entry=2&amp;sticky=false&amp;w=false&quot;,&quot;user_id&quot;:null}}" data-hydro-view-hmac="da27f168452f5401cc39365cfa7bab7808b0055f832c759ca5c44e87de6005c1">
            <div class="render-wrapper ">
    <div class="render-container js-render-target is-render-automatic is-render-requested is-render-ready" data-identity="0c9cf4f0-1a12-4ea2-bad9-022aa74c4a2c" data-host="https://viewscreen.githubusercontent.com" data-type="img" style="height: 510px;">
      <span data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="64" height="64" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="octospinner mx-auto anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
      <div class="render-viewer-error">Sorry, something went wrong. <a class="Link--inTextBlock" href="https://github.com/Bansodeprasad/Color-Detection-/diffs?bytes=2054&amp;commit=d2de12dff17aff39101e04671cb502efb8330376&amp;lines=70&amp;responsive=true&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;start_entry=2&amp;sticky=false&amp;w=false">Reload?</a></div>
      <div class="render-viewer-fatal">Sorry, we cannot display this file.</div>
      <div class="render-viewer-invalid">Sorry, this file is invalid so it cannot be displayed.</div>
      <iframe class="render-viewer " src="./color_detection_files/img(2).html" sandbox="allow-scripts allow-same-origin allow-top-navigation" title="File display" name="0c9cf4f0-1a12-4ea2-bad9-022aa74c4a2c">
          Viewer requires iframe.
      </iframe>
    </div>
  </div>
 

    </div>
  </div>
</copilot-diff-entry>

  <copilot-diff-entry data-file-path="pic3.jpg" data-disabled="">
  <div id="diff-929c963f641a0c6889cdb834f314c363d0db29991b97c835c0b18fa5b148ff95" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
               display-rich-diff
              
              
              " data-file-type=".jpg" data-file-deleted="false" data-tagsearch-path="pic3.jpg" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch" data-path="pic3.jpg" data-short-path="929c963" data-anchor="diff-929c963f641a0c6889cdb834f314c363d0db29991b97c835c0b18fa5b148ff95" data-file-type=".jpg" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">Binary file added</span>
          <span class="diffstat" aria-hidden="true">
            BIN
              <span class="color-fg-success">
                +1.95 MB

              </span>
          </span>

        
<span class="Truncate">
  <a title="pic3.jpg" class="Link--primary Truncate-text" href="https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376#diff-929c963f641a0c6889cdb834f314c363d0db29991b97c835c0b18fa5b148ff95">pic3.jpg</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="pic3.jpg" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">








            <span class="BtnGroup min-width-0">
                <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-prose-diff-toggle-form" data-turbo="false" action="https://github.com/Bansodeprasad/Color-Detection-/diffs/5?commit=d2de12dff17aff39101e04671cb502efb8330376&amp;name=main&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;source=true&amp;w=false" accept-charset="UTF-8" method="get">                  <button class="btn btn-sm BtnGroup-item tooltipped tooltipped-s source js-source" aria-label="Display the source diff" type="submit" data-disable-with="">
                          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
                  </button>
</form>                  <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-prose-diff-toggle-form" data-turbo="false" action="https://github.com/Bansodeprasad/Color-Detection-/diffs/5?commit=d2de12dff17aff39101e04671cb502efb8330376&amp;name=main&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;short_path=929c963&amp;w=false" accept-charset="UTF-8" method="get">                    <button class="btn btn-sm BtnGroup-item tooltipped tooltipped-s rendered js-rendered selected" aria-current="true" aria-label="Display the rich diff" type="submit" data-disable-with="">
                            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file">
    <path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
                    </button>
</form>            </span>



          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:max-content; min-width:185px; z-index:99; right: -4px;" role="menu">
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/Bansodeprasad/Color-Detection-/blob/d2de12dff17aff39101e04671cb502efb8330376/pic3.jpg" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            </details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:null,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/diffs?bytes=2054&amp;commit=d2de12dff17aff39101e04671cb502efb8330376&amp;lines=70&amp;responsive=true&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;start_entry=2&amp;sticky=false&amp;w=false&quot;,&quot;user_id&quot;:null}}" data-hydro-view-hmac="da27f168452f5401cc39365cfa7bab7808b0055f832c759ca5c44e87de6005c1">
            <div class="render-wrapper ">
    <div class="render-container js-render-target is-render-automatic is-render-requested is-render-ready" data-identity="a99457b5-ce0f-43fa-b8e3-4902ce9a4dd8" data-host="https://viewscreen.githubusercontent.com" data-type="img" style="height: 510px;">
      <span data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="64" height="64" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="octospinner mx-auto anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
      <div class="render-viewer-error">Sorry, something went wrong. <a class="Link--inTextBlock" href="https://github.com/Bansodeprasad/Color-Detection-/diffs?bytes=2054&amp;commit=d2de12dff17aff39101e04671cb502efb8330376&amp;lines=70&amp;responsive=true&amp;sha1=1724f953f3d24296dd1c1c2d1193328460a204ed&amp;sha2=d2de12dff17aff39101e04671cb502efb8330376&amp;start_entry=2&amp;sticky=false&amp;w=false">Reload?</a></div>
      <div class="render-viewer-fatal">Sorry, we cannot display this file.</div>
      <div class="render-viewer-invalid">Sorry, this file is invalid so it cannot be displayed.</div>
      <iframe class="render-viewer " src="./color_detection_files/img(3).html" sandbox="allow-scripts allow-same-origin allow-top-navigation" title="File display" name="a99457b5-ce0f-43fa-b8e3-4902ce9a4dd8">
          Viewer requires iframe.
      </iframe>
    </div>
  </div>
 

    </div>
  </div>
</copilot-diff-entry>



</div>


</div>

<button type="button" class="js-toggle-all-file-notes" data-hotkey="i" style="display:none">Toggle all file notes</button>

<button type="button" class="js-toggle-all-file-annotations" data-hotkey="a" style="display:none">Toggle all file annotations</button>

<svg aria-hidden="true" width="100px" height="84px" viewBox="0 0 340 84" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="diff-placeholder-svg position-absolute bottom-0">
  <defs>
    <clippath id="diff-placeholder">
      <rect x="0" y="0" width="67.0175439" height="11.9298746" rx="2"></rect>
      <rect x="18.9473684" y="47.7194983" width="100.701754" height="11.9298746" rx="2"></rect>
      <rect x="0" y="71.930126" width="37.8947368" height="11.9298746" rx="2"></rect>
      <rect x="127.017544" y="48.0703769" width="53.3333333" height="11.9298746" rx="2"></rect>
      <rect x="187.719298" y="48.0703769" width="72.9824561" height="11.9298746" rx="2"></rect>
      <rect x="76.8421053" y="0" width="140.350877" height="11.9298746" rx="2"></rect>
      <rect x="17.8947368" y="23.8597491" width="140.350877" height="11.9298746" rx="2"></rect>
      <rect x="166.315789" y="23.8597491" width="173.684211" height="11.9298746" rx="2"></rect>
    </clippath>

    <lineargradient id="animated-diff-gradient" x1="0" x2="0" y1="0" y2="1" spreadMethod="reflect">
      <stop offset="0" stop-color="#eee"></stop>
      <stop offset="0.2" stop-color="#eee"></stop>
      <stop offset="0.5" stop-color="#ddd"></stop>
      <stop offset="0.8" stop-color="#eee"></stop>
      <stop offset="1" stop-color="#eee"></stop>
      <animatetransform attributeName="y1" values="0%; 100%; 0" dur="1s" repeatCount="3"></animatetransform>
      <animatetransform attributeName="y2" values="100%; 200%; 0" dur="1s" repeatCount="3"></animatetransform>
    </lineargradient>
  </defs>
</svg>


            <div id="all_commit_comments" class="js-quote-selection-container" data-quote-markdown=".js-comment-body">
  <div class="mb-1 mb-md-3">
    
<div id="partial-visible-comments-header" class="d-flex flex-items-center flex-column-reverse flex-md-row">
  <h3 class="h4 flex-auto text-md-left text-center">
    0 comments
    on commit <code class="commit-sha">d2de12d</code>
  </h3>

  <div class="flex-shrink-0 mb-2 mb-md-0">
    
  </div>
</div>

  </div>

  <div id="comments" class="comment-holder ml-0 pl-0 ml-md-6 pl-md-3">
    

  <!-- Rendered timeline since 2024-03-10 01:25:54 -->
  <div id="partial-timeline-marker" class="js-timeline-marker js-socket-channel js-updatable-content" data-channel="eyJjIjoicmVwbzo3Njk4NjE4OTA6Y29tbWl0OmQyZGUxMmRmZjE3YWZmMzkxMDFlMDQ2NzFjYjUwMmVmYjgzMzAzNzYiLCJ0IjoxNzQxMjQzOTM5fQ==--df1549424eba56724e5a9b2bcbb112edbf3b09a5c91b3bfb4b30ba2bfcc9e4e9" data-url="/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376/show_partial?partial=commit%2Ftimeline_marker&amp;since=1710062754" data-last-modified="Sun, 10 Mar 2024 09:25:54 GMT">

  </div>

  </div>

  

    Please
  <a rel="nofollow" class="Link--inTextBlock" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;commit comment&quot;,&quot;repository_id&quot;:769861890,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/Bansodeprasad/Color-Detection-/commit/d2de12dff17aff39101e04671cb502efb8330376&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="c3eef93f034d9aad50848063f4198a88488a7da39b027b6d96c77fd4fc1ca796" href="https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FBansodeprasad%2FColor-Detection-%2Fcommit%2Fd2de12dff17aff39101e04671cb502efb8330376">sign in</a> to comment.

</div>

</div>
</div>  </diff-layout>


</div>


  </div>

</turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
</a>
      <span>
        © 2025 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>




    </div>

    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true">loaded diff for colors.csv</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


</body></html>